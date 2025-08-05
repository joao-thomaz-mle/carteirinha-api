import json
import logging

from app.utils.config import load_config

config = load_config()


class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "name": record.name,
            "message": record.getMessage(),
            "filename": record.filename,
            "lineno": record.lineno,
        }
        return json.dumps(log_record, ensure_ascii=False)


def get_logger(name: str):
    log_level = logging.DEBUG if config["LOG_LEVEL"] == "hml" else logging.INFO

    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    formatter = JSONFormatter(datefmt="%Y-%m-%dT%H:%M:%S")

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if logger.hasHandlers():
        logger.handlers = [console_handler]

    return logger
