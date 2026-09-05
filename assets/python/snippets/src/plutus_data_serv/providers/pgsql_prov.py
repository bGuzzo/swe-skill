from threading import Lock

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session

from plutus_data_serv.configs import SETTINGS, get_logger
from plutus_data_serv.providers.base_prov import BaseProv
from plutus_data_serv.utils.decorators import retry_conn
from plutus_data_serv.utils.singleton import SingletonMeta

LOGGER = get_logger()


class PgsqlProv(BaseProv, metaclass=SingletonMeta):
    def __init__(self) -> None:
        super().__init__()
        self._pgsql_host: str = SETTINGS.PGSQL_HOSTS
        self._pgsql_port: int = SETTINGS.PGSQL_PORT
        self._pgsql_db: str = SETTINGS.PGSQL_DB
        self._pgsql_user: str = SETTINGS.PGSQL_USERNAME
        self._pgsql_password: str = SETTINGS.PGSQL_PASSWORD
        self._pgsql_conn_str: str = (
            f"postgresql+psycopg://{self._pgsql_user}:{self._pgsql_password}@{self._pgsql_host}:{self._pgsql_port}/{self._pgsql_db}"
        )
        self._engine: Engine | None = None
        self._engine_lock: Lock = Lock()
        self._init_engine()

    @retry_conn
    def _init_engine(self) -> None:
        try:
            with self._engine_lock:
                if self._engine:
                    return

                LOGGER.info(f"Connecting to {self._pgsql_conn_str}")
                self._engine = create_engine(self._pgsql_conn_str)
                self._engine.connect()
                LOGGER.info(f"Successfully connected to {self._pgsql_conn_str}")
        except:
            LOGGER.exception(f"Unable to connect to PgSQL at: {self._pgsql_conn_str}")
            raise

    def get_session(self) -> Session:
        """Return a new Session object"""
        try:
            self._init_engine()
            with self._engine_lock:
                session: Session = Session(self._engine)
                LOGGER.info("Created SQLAlchemy Session")
                return session
        except:
            LOGGER.exception(f"Unable to create session for connection: {self._pgsql_conn_str}")
            raise

    def on_exit(self) -> None:
        LOGGER.info(f"Closing engine connection to: {self._pgsql_conn_str}")
        if self._engine:
            self._engine.dispose(close=True)
            self._engine = None
        LOGGER.info("Engine closed")
