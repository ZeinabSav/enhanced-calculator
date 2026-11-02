from logger import LoggingObserver

def test_logger_creation():
    logger = LoggingObserver()
    assert logger is not None