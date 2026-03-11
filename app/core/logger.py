from logging import getLogger, INFO, ERROR, WARNING, DEBUG, Formatter, StreamHandler


class Logger:
    def __init__(self, logger):
        self.logger = logger
        self.logger.setLevel(INFO)
        formatter = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        stream_handler = StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

    def info(self, message: str):
        self.logger.info(message)

    def error(self, message: str):
        self.logger.error(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def debug(self, message: str):
        self.logger.debug(message)


logger = Logger(getLogger(__name__))
