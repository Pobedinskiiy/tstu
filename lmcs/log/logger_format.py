import logging


class CustomFormatter(logging.Formatter):
    black = "\x1b[1;30m"
    red = "\x1b[1;31m"
    green = "\x1b[1;32m"
    yellow = "\x1b[1;33m"
    blue = "\x1b[1;34m"
    violet = "\x1b[1;35m"
    turquoise = "\x1b[1;36m"
    grey = "\x1b[1;37m"
    white = "\x1b[1;38m"
    reset = "\x1b[0m"
    format = "[%(asctime)s] [%(levelname)s] [%(module)s.%(funcName)s] %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: violet + format + reset,
        logging.CRITICAL: red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
