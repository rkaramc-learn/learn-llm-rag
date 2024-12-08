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
