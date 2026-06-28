from logging_config import logger

def info(message: str):
    """
    Logs an informational message to the console and log file.
    """
    logger.info(message)


def warning(message: str):
    """
    Logs a warning message to the console and log file.
    """
    logger.warning(message)


def error(message: str):
    """
    Logs an error message to the console and log file.
    """
    logger.error(message)