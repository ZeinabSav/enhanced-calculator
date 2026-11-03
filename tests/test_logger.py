from logger import LoggingObserver


def test_logger_exists():
    logger = LoggingObserver()
    assert logger is not None


def test_logger_has_update():
    logger = LoggingObserver()
    assert hasattr(logger, "update")