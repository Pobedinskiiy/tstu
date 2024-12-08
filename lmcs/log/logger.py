import logging

from .logger_format import CustomFormatter

def init_logging() -> None:
    handler = logging.StreamHandler()
    handler.setFormatter(CustomFormatter())

    logger = logging.getLogger()
    logger.addHandler(handler)

    logger.setLevel(logging.DEBUG)