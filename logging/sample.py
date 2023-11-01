from logging import getLogger

logger = getLogger(__name__)

def do_something():
    logger.debug("debug message from sample.py")
    logger.info("info message from sample.py")
    logger.warning("warning message from sample.py")