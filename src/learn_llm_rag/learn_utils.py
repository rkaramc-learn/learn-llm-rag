import logging
import time

logger = logging.getLogger(__name__)


class Timer:
    def __init__(self, name, _logger=None):
        self.start_time = None
        self.name = name
        self._logger = _logger or logger

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.perf_counter()
        duration = end_time - self.start_time
        self._logger.info(f"{duration:.2f}s - {self.name}")
        return False  # exception not propagating earlier with `return duration`


class ConsoleFormatter(logging.Formatter):
    def format(self, record):
        # Save the original exc_info and exc_text
        original_exc_info = record.exc_info
        original_exc_text = record.exc_text

        # Clear exc_info and exc_text for console output
        record.exc_info = None
        record.exc_text = None

        # Format the record
        result = super().format(record)

        # Restore the original exc_info and exc_text
        record.exc_info = original_exc_info
        record.exc_text = original_exc_text

        return result
