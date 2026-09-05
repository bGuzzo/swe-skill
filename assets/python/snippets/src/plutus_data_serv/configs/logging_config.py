import logging

from plutus_data_serv.configs.settings_config import SETTINGS
from plutus_data_serv.utils.singleton import SingletonMeta


class LogSingletonConfig(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self._log_format = SETTINGS.LOG_FORMAT
        self._log_level = SETTINGS.LOG_LEVEL

        logging.basicConfig(format=self._log_format, level=self._log_level)

        # Avoid calling get_logger(), will trigger recursion
        self._logger = logging.getLogger(__name__)
        self._logger.info(f"Loaded environment {SETTINGS.ENVIRONMENT}")
        self._logger.info(f"Loaded settings dict: {SETTINGS}")
        self._logger.info(f"Initialized logging configuration with level: {self._log_level}, format: {self._log_format}")
        del self._logger


def get_logger() -> logging.Logger:
    LogSingletonConfig()
    return logging.getLogger(__name__)
