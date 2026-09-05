import logging
from typing import TYPE_CHECKING, TypeVar

from tenacity import before_sleep_log, retry, stop_after_delay, wait_exponential

from plutus_data_serv.configs import get_logger

if TYPE_CHECKING:
    from collections.abc import Callable

LOGGER = get_logger()

# Pre-configure and define your custom decorator alias
retry_conn = retry(
    stop=stop_after_delay(128),
    wait=wait_exponential(multiplier=2, min=5, max=10),
    before_sleep=before_sleep_log(LOGGER, logging.WARNING),
    reraise=True,
)

T = TypeVar("T", bound=type)

# Consatnts for later import
PROFILE_NAME_ARG: str = "__profile_name__"
PROFILE_ON_ARG: str = "__profile_on__"


def profile(name: str, on: bool = True) -> Callable[[T], T]:
    """
    Decorator to mark a provider class with a profile condition.

    Args:
        name (str): The profile stage/environment name (e.g., 'local', 'cloud').
        on (bool): If True, the provider is enabled for this profile.
                   If False, the provider is disabled for this profile.
    """

    def decorator(cls: T) -> T:
        # Ruff ignore to avoid fixes
        setattr(cls, "__profile_name__", name)  # noqa: B010
        setattr(cls, "__profile_on__", on)  # noqa: B010
        return cls

    return decorator
