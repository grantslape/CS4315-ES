import logging
import sys
from logging.handlers import TimedRotatingFileHandler
from settings import LOG_LEVEL

FORMATTER = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
FILE_NAME = 'logs/python.log'


def get_console_handler():
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(FORMATTER)
    return handler


def get_file_handler():
    handler = TimedRotatingFileHandler(FILE_NAME, when='midnight')
    handler.setFormatter(FORMATTER)
    return handler


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)

    logger.setLevel(LOG_LEVEL)

    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.propagate = False

    return logger
