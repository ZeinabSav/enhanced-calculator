from logger import LoggingObserver


def test_logger_exists():
    logger = LoggingObserver()
    assert logger is not None


def test_logger_has_update():
    logger = LoggingObserver()
    assert hasattr(logger, "update")


def test_multiple_logger_objects():
    logger1 = LoggingObserver()
    logger2 = LoggingObserver()

    assert logger1 is not None
    assert logger2 is not None