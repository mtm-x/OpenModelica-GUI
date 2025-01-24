import logging
import os


def setup_logging(log_file="logs/OPLauncher.log"):
    """
    Configure the logging system.

    Logging is written to both a log file and the console. The logging level is
    set to DEBUG to capture detailed messages for debugging and analysis.

    """
    # Ensure the directory for the log file exists
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logging.basicConfig(
        level=logging.DEBUG,  # Capture all log levels (DEBUG, INFO, etc.)
        format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
        datefmt="%Y-%m-%d %H:%M:%S",  # Timestamp format
        handlers=[
            logging.FileHandler(log_file),  # Write logs to the specified file
            logging.StreamHandler()  # Also output logs to the console
        ]
    )
    logging.getLogger('matplotlib').setLevel(logging.WARNING)
    logging.getLogger('scipy').setLevel(logging.ERROR)
    logging.info(
        "Logging system initialized. Writing logs to '%s'", log_file
    )
