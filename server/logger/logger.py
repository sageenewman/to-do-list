from typing import NoReturn
from loguru import logger
from logger.logger_config import LOG_FILE_FORMAT, MAX_SIZE_FILE, LOG_FORMAT


def initialize_logger() -> NoReturn:
    logger.add(LOG_FILE_FORMAT,
               format=LOG_FORMAT,
               retention=MAX_SIZE_FILE,
               colorize=True,
               serialize=True,
               enqueue=True)
