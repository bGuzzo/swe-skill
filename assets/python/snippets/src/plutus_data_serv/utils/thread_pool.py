import atexit
import os
from concurrent.futures import ThreadPoolExecutor

from plutus_data_serv.configs import SETTINGS, get_logger
from plutus_data_serv.utils.singleton import SingletonMeta

LOGGER = get_logger()


class GlobalThreadPool(metaclass=SingletonMeta):
    """
    A global, application-wide thread pool singleton.
    Configured based on OS CPU count and the setting THREADS_MUL.
    """

    def __init__(self) -> None:
        num_cores = os.cpu_count() or 1
        self._max_workers = num_cores * SETTINGS.THREADS_MUL

        LOGGER.info(f"Initializing GlobalThreadPool with {self._max_workers} worker threads (Cores: {num_cores}, Multiplier: {SETTINGS.THREADS_MUL})")
        self._executor = ThreadPoolExecutor(max_workers=self._max_workers, thread_name_prefix="GlobalThreadPool")

        # Register exit handler to clean up resources gracefully
        atexit.register(self._on_exit)

    def get_executor(self) -> ThreadPoolExecutor:
        """Retrieve the underlying ThreadPoolExecutor."""
        return self._executor

    def _on_exit(self) -> None:
        """Gracefully shut down the thread pool on application exit."""
        LOGGER.info("Shutting down GlobalThreadPool...")
        self._executor.shutdown(wait=True)
        LOGGER.info("GlobalThreadPool shutted down successfully")
