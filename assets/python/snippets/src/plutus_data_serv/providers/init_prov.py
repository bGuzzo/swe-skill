# import random
# import threading
import atexit
import importlib
import inspect
from typing import TYPE_CHECKING

from plutus_data_serv.configs import SETTINGS, get_logger
from plutus_data_serv.providers.base_prov import BaseProv
from plutus_data_serv.utils.decorators import PROFILE_NAME_ARG, PROFILE_ON_ARG
from plutus_data_serv.utils.thread_pool import GlobalThreadPool

if TYPE_CHECKING:
    from concurrent.futures import Future, ThreadPoolExecutor


LOGGER = get_logger()


def _get_prov_class_to_init(
    package_name: str, base_class: type, profile_name_arg: str = PROFILE_NAME_ARG, profile_on_arg: str = PROFILE_ON_ARG
) -> list[type]:
    package = importlib.import_module(package_name)

    # Iterate only onver the first package layer, no bupackages
    matched_classes: list[type] = []
    for _, cls_obj in inspect.getmembers(package, inspect.isclass):
        if (not issubclass(cls_obj, base_class)) or (cls_obj is base_class):
            continue

        # If @profile is missing load anyway
        if hasattr(cls_obj, profile_name_arg) and hasattr(cls_obj, profile_on_arg):
            cls_obj_profile_name: str = getattr(cls_obj, profile_name_arg)
            cls_obj_profile_on: bool = getattr(cls_obj, profile_on_arg)

            if not cls_obj_profile_name:
                # Ignore malformed decorators
                continue

            if cls_obj_profile_name.lower() == SETTINGS.ENVIRONMENT.lower() and cls_obj_profile_on:
                # Append only if profile match and it is on
                matched_classes.append(cls_obj)

        else:
            matched_classes.append(cls_obj)

    LOGGER.info(f"Found {len(matched_classes)} marked to be loaded inside {package_name} for env {SETTINGS.ENVIRONMENT}")
    LOGGER.info(f"Providers found: {[cls_obj.__name__ for cls_obj in matched_classes]}")
    return matched_classes


def init_providers() -> None:
    """Multihreading inizialization of providers"""
    try:
        providers_cls: list[type] = _get_prov_class_to_init(package_name="plutus_data_serv.providers", base_class=BaseProv)
    except Exception:
        LOGGER.exception("Unable to load providers, applicatrion start aborted")
        raise

    t_pool: ThreadPoolExecutor = GlobalThreadPool().get_executor()
    future_list: list[Future[BaseProv]] = []
    LOGGER.info("Inizializing providers")
    for cls_obj in providers_cls:
        future_list.append(t_pool.submit(cls_obj))

    for future_obj in future_list:
        cls_obj_inst: BaseProv = future_obj.result()
        atexit.register(cls_obj_inst.on_exit)
        LOGGER.info(f"Provided of type {type(cls_obj_inst).__name__} initlized and exit function registered")

    LOGGER.info("All providers intialized successfully")
