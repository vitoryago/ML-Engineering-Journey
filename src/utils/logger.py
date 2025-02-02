# src/utils/logger.py

import logging
import sys
from pathlib import Path
from typing import Optional
from datetime import datetime

def setup_logger(
        name: str,
        log_file: Optional[Path] = None,
        level: int = logging.INFO
) -> logging.Logger:
    """
    Creates and configures a logger for our ML application.

    This function sets up a logger that can write to both console and file,
    which is essential for ML applications where we need to track model behavior,
    data processing, and system interactions.

    Args:
        name (str): Name of the logger, usually __name__ from the calling module
        log_file(Optional[Path]): Path to the log file. If None, logs only to console.
        level (int): Logging level for the logger. Default is logging.INFO.
    
    Returns:
        logging.Logger: Configured logger object for logging messages.
    
    
    Example:
        >>> logger = setup_logger(__name__, log_file='logs/app.log')
        >>> logger.info("Processing blood test data")
        2024-02-02 10:34:45 - Processing blood test data
    """

    # Create logger with given name
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create formatters for our logs
    # We include timestamp, logger name, and message for proper tracking
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Always set up console handler for development visibility
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # If log file path is provided, set up file handler
    if log_file:
        # Create log directory if it doesn't exist
        log_file.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # Prevent log messages form being propagated to parent loggers
    logger.propagate = False

    return logger