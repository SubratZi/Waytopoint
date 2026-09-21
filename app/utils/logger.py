import logging

from app.config import settings

logging.basicConfig(
    level = settings.log_level,
    format = "%(asctime)s %(levelname)-7s %(name)s: %(message)s",
)

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)