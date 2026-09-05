from plutus_data_serv.configs import get_logger
from plutus_data_serv.utils.singleton import SingletonMeta

LOGGER = get_logger()


class BaseProv(metaclass=SingletonMeta):
    def __init__(self) -> None:
        super().__init__()
        LOGGER.info(f"Initialized provider {type(self).__name__}")

    # Use the main thread to handle termination
    def on_exit(self) -> None:
        """A simple exit function, it is ment to be registered only on the main thread"""
        raise NotImplementedError(f"Class of type {type(self).__name__} does not implement _on_exit function.")
