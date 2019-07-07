import logging


class Monitor:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.debug(f"{self} has been initialized.")
