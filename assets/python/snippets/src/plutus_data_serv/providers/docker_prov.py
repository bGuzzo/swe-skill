from pathlib import Path

from python_on_whales import DockerClient

from plutus_data_serv.configs import SETTINGS, get_logger
from plutus_data_serv.providers.base_prov import BaseProv
from plutus_data_serv.utils.decorators import profile
from plutus_data_serv.utils.singleton import SingletonMeta

LOGGER = get_logger()


@profile(name="local", on=True)
class DockerProv(BaseProv, metaclass=SingletonMeta):
    def __init__(self) -> None:
        super().__init__()

        if not SETTINGS.DOCKER_CONF_PAHT:
            raise ValueError("Found null or empty DOCKER_CONF_PAHT variable")

        self._compose_path: Path = Path(SETTINGS.DOCKER_CONF_PAHT)
        if not self._compose_path.exists():
            raise ValueError(f"{SETTINGS.DOCKER_CONF_PAHT} is not a valid path")

        self._docker = DockerClient(compose_files=[str(self._compose_path)])
        self._start()

    def _start(self) -> None:
        try:
            if self._docker.ps():
                LOGGER.warning(f"Docker Compose for file {self._compose_path!s} is already up")
            else:
                self._docker.compose.up(detach=True)
                LOGGER.info("Docker Compose started")
        except Exception:
            LOGGER.exception(f"Unable to start Docker Compose for file {self._compose_path!s}, please check it")
            raise

    def on_exit(self) -> None:
        try:
            self._docker.compose.down(volumes=False, remove_orphans=True)
            LOGGER.info("Docker Compose shut down")
        except Exception:
            LOGGER.exception(f"Unable to shut down Docker Compose for file {self._compose_path!s}, exiting anyway")
