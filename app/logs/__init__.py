import logging  # Standard Python module for logging events and messages.

def setup_logs():
    """Configure the logging settings for the application."""
    logging.basicConfig(
        filename='calculator.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

__all__ = ['setup_logs']  # This allows the import statement to work correctly.
