import logging

class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        # Create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        # Add handler to the logger
        self.logger.addHandler(ch)

    def log_info(self, message):
        try:
            if not isinstance(message, str):
                raise ValueError('Message must be a string')
            self.logger.info(message)
        except Exception as e:
            self.logger.error(f'Error logging info: {e}')

    def log_debug(self, message):
        try:
            if not isinstance(message, str):
                raise ValueError('Message must be a string')
            self.logger.debug(message)
        except Exception as e:
            self.logger.error(f'Error logging debug: {e}')

    def log_error(self, message):
        try:
            if not isinstance(message, str):
                raise ValueError('Message must be a string')
            self.logger.error(message)
        except Exception as e:
            self.logger.error(f'Error logging error: {e}')