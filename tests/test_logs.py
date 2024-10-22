import pytest # type: ignore
from app.logs import setup_logs

def test_setup_logging():
    """Test that setup_logging runs without raising any exceptions."""
    try:
        setup_logs()
    except Exception as e:
        pytest.fail(f"setup_logging raised an exception: {e}")