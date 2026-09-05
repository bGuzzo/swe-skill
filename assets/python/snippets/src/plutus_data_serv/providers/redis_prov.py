import redis

from plutus_data_serv.configs import SETTINGS, get_logger
from plutus_data_serv.providers.base_prov import BaseProv
from plutus_data_serv.utils.decorators import retry_conn
from plutus_data_serv.utils.singleton import SingletonMeta

LOGGER = get_logger()


class RedisProv(BaseProv, metaclass=SingletonMeta):
    def __init__(self) -> None:
        super().__init__()
        self._redis_host: str = SETTINGS.REDIS_HOST
        self._redis_port: int = SETTINGS.REDIS_PORT
        self._session: redis.Redis = self._connect()

    @retry_conn
    def _connect(self) -> redis.Redis:
        LOGGER.info(f"Connecting to Redis on {self._redis_host}:{self._redis_port}")
        redis_session = redis.Redis(host=self._redis_host, port=self._redis_port)
        LOGGER.info(f"Connection established to Redis on {self._redis_host}:{self._redis_port}")
        return redis_session

    def get_session(self) -> redis.Redis:
        return self._session

    def on_exit(self) -> None:
        self._session.close()
        LOGGER.info(f"Connection to Redis closed from {self._redis_host}:{self._redis_port}")
