"""
This module creates the logger for vRA API Client
"""
import logging
import logging.handlers
from sys import platform

# Logger constants
LOGGER_FILE_NAME = "/var/log/vraapiclient.log"
LOG_FILE_MAX_BYTES = 51200
LOG_FILE_BACKUP_COUNT = 3
LOGGER_NAME = "vRAAPIClient"
LOGGER_INIT=False

def setup_custom_logger(name=LOGGER_NAME, source="default"):
    """
    Creates logger for vRA API client
    """
    global LOGGER_INIT
    formatter = logging.Formatter('%(asctime)s:%(name)s[%(process)d]:\
                    %(levelname)s:%(funcName)s():%(lineno)s - %(message)s')
    if source == "console":
        handler = logging.StreamHandler()
    elif source == "syslog":
        formatter = logging.Formatter('%(name)s[%(process)d]:%(levelname)s:\
                        %(funcName)s():%(lineno)s - %(message)s')
        if platform == "linux" or platform == "linux2": # linux
            address = '/dev/log'
        elif platform == "darwin": # OS X
            address = '/var/run/syslog'
        handler = logging.handlers.SysLogHandler(address=address)
    else:
        handler = logging.handlers.RotatingFileHandler(filename=LOGGER_FILE_NAME, \
                    maxBytes=LOG_FILE_MAX_BYTES, backupCount=LOG_FILE_BACKUP_COUNT)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    LOGGER_INIT=True
    return logger

def getLogger():
    """
        returns the custom logger, creates if its not already initialized
    """
    if LOGGER_INIT is True:
        return logging.getLogger(LOGGER_NAME)
    else:
        return setup_custom_logger()