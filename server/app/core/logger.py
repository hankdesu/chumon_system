import logging


def setup_logging():
    LOG_FORMAT = "[%(asctime)s] %(levelname)s - %(message)s"
    custom_formatter = logging.Formatter(LOG_FORMAT)

    logger_names = ["uvicorn", "uvicorn.error", "uvicorn.access"]

    for name in logger_names:
        logger = logging.getLogger(name)
        for handler in logger.handlers:
            handler.setFormatter(custom_formatter)


error_logger = logging.getLogger("uvicorn.error")
access_logger = logging.getLogger("uvicorn.access")
