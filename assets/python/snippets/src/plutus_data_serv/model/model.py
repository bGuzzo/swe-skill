import uuid
from datetime import datetime  # noqa: TC003
from typing import ClassVar

from sqlalchemy import DateTime, ForeignKey, Numeric, String, Text, Uuid, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    # Override MyPy type checking
    __table_args__: ClassVar[dict[str, str]] = {"schema": "public"}  # type: ignore[misc]

    # ID (not PK)
    uuid: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=False, unique=True, index=True, default=uuid.uuid4, nullable=False)

    # Common audit timestamps automatically managed by PostgreSQL
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class Ticker(Base):
    __tablename__ = "ticker"

    code: Mapped[str] = mapped_column(String, primary_key=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)


# ==============================================================================
# PRODUCTION WARNING & SCHEDULER NOTE FOR DATA PIPELINE
# ==============================================================================
# Source: yfinance (downloaded with auto_adjust=True)
# Target Storage: PostgreSQL Raw Ticker Store
#
# 1. PRICE FIELD ADJUSTMENT:
#    'open', 'high', 'low', 'close' are PRE-ADJUSTED by yfinance for corporate
#    actions (splits + dividends). The 'close' column represents Adjusted Close.
#
# 2. THE VOLUME ANOMALY (CRITICAL FOR LIVE EX):
#    yfinance DOES NOT adjust the 'volume' column when auto_adjust=True.
#    - Historical volumes remain unscaled relative to adjusted historical prices.
#    - Since downstream torch data loader computes Log Volume Intensity over SMA20
#      [log(Vol / SMA20(Vol))], the scale factor cancels out mathematically
#      WITHOUT mutating raw pgsql volume data.
#    - Leave pgsql volume raw to maintain alignment with live Alpaca socket streams.
#
# 3. LIVE EXECUTION TRANSLATION LAYER:
#    The Torch Diffusion Transformer (DiT) trains on stationary features, but the
#    final inference target must be projected onto the CURRENT LIVE UNADJUSTED RAW
#    PRICE matching the Alpaca order book.
#    Formula: Execution Target Price = Alpaca_Live_Raw_Close * exp(Model_Pred_Log_Return)
# ==============================================================================
class OhlcvData(Base):
    __tablename__ = "ohlcv_data"

    # Composed PK
    ticker_code: Mapped[str] = mapped_column(String, ForeignKey("public.ticker.code", ondelete="RESTRICT"), primary_key=True)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), primary_key=True)  # Allow for fine grade 1d/1h/4h data
    interval: Mapped[str] = mapped_column(String, primary_key=True)  # yFinance interval (1d, 1h, 4mo)

    # Use auto_adjust=True in yFinance to download them
    adj_open: Mapped[float] = mapped_column(Numeric)
    adj_high: Mapped[float] = mapped_column(Numeric)
    adj_low: Mapped[float] = mapped_column(Numeric)
    adj_close: Mapped[float] = mapped_column(Numeric)
    volume: Mapped[float] = mapped_column(Numeric)


class Dataset(Base):
    __tablename__ = "dataset"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Many-to-Many Relationship to Ticker (Unidirectional via secondary class table)
    tickers: Mapped[list[Ticker]] = relationship(secondary="public.dataset_ticker")


class DatasetTicker(Base):
    __tablename__ = "dataset_ticker"

    dataset_id: Mapped[str] = mapped_column(String, ForeignKey("public.dataset.id", ondelete="RESTRICT"), primary_key=True)
    ticker_code: Mapped[str] = mapped_column(String, ForeignKey("public.ticker.code", ondelete="RESTRICT"), primary_key=True)
