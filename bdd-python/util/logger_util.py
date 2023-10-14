#!/usr/bin/env python3
"""
Logger utility
"""
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
#                                                                               -
#  Python dual-logging setup (console and log file),                            -
#  supporting different log levels and colorized output                         -
#                                                                               -
# -------------------------------------------------------------------------------

import logging

# Imports
import sys
from datetime import datetime


# Logging formatter supporting colorized output
class LogFormatter(logging.Formatter):
    """
    Class for log formatting
    """

    COLOR_CODES = {
        logging.CRITICAL: "\033[1;35m",  # bright/bold magenta
        logging.ERROR: "\033[1;31m",  # bright/bold red
        logging.WARNING: "\033[1;33m",  # bright/bold yellow
        logging.INFO: "\033[0;37m",  # white / light gray
        logging.DEBUG: "\033[1;30m",  # bright/bold black / dark gray
    }

    RESET_CODE = "\033[0m"

    def __init__(self, color, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = color

    def format(self, record, *args, **kwargs):
        if self.color and record.levelno in self.COLOR_CODES:
            record.color_on = self.COLOR_CODES[record.levelno]
            record.color_off = self.RESET_CODE
        else:
            record.color_on = ""
            record.color_off = ""
        return super().format(record, *args, **kwargs)


# Setup logging
def get_logger(
    name=None,
    console_log_output="stdout",
    console_log_level="info",
    console_log_color=True,
    logfile_file=f"testSuite-{datetime.now().strftime('%d%m%Y%H%M%S')}.log",
    logfile_log_level="info",
    logfile_log_color=False,
    log_line_template="%(color_on)s %(asctime)s [%(levelname)s %(module)s:%(lineno)d] %(message)s%(color_off)s",
):
    # %(color_on)s[%(created)d] [%(threadName)s] [%(levelname)-8s] %(message)s%(color_off)s

    # Create logger
    # For simplicity, we use the root logger, i.e. call 'logging.getLogger()'
    # without name argument. This way we can simply use module methods
    # for logging throughout the script. An alternative would be exporting
    # the logger, i.e. 'global logger; logger = logging.getLogger("<name>")'
    _logger = logging.getLogger(name or __name__)

    # Set global log level to 'debug' (required for handler levels to work)
    _logger.setLevel(logging.DEBUG)

    selenium_logger = logging.getLogger("seleniumwire")
    selenium_logger.setLevel(logging.ERROR)

    # Create console handler
    console_log_output = console_log_output.lower()
    if console_log_output == "stdout":
        console_log_output = sys.stdout
    elif console_log_output == "stderr":
        console_log_output = sys.stderr
    else:
        print("Failed to set console output: invalid output: '%s'" % console_log_output)
        return False
    console_handler = logging.StreamHandler(console_log_output)

    # Set console log level
    try:
        console_handler.setLevel(console_log_level.upper())  # only accepts uppercase level names
    except Exception as e:
        print(f"Failed to set console log level: invalid level: " f"{console_handler} {e}")
        return False

    # Create and set formatter, add console handler to logger
    console_formatter = LogFormatter(fmt=log_line_template, color=console_log_color)
    console_handler.setFormatter(console_formatter)
    _logger.addHandler(console_handler)

    # Create log file handler
    try:
        logfile_handler = logging.FileHandler(logfile_file)
    except Exception as exception:
        print("Failed to set up log file: %s" % str(exception))
        return False

    # Set log file log level
    try:
        logfile_handler.setLevel(logfile_log_level.upper())  # only accepts uppercase level names
    except Exception as e:
        print(f"Failed to set log file log level: invalid level: '{logfile_log_level}' {e}")
        return False

    # Create and set formatter, add log file handler to logger
    logfile_formatter = LogFormatter(fmt=log_line_template, color=logfile_log_color)
    logfile_handler.setFormatter(logfile_formatter)
    _logger.addHandler(logfile_handler)

    # Success
    return _logger


# Main function
def main():
    # Setup logging
    _logger = get_logger(__name__)

    # Log some messages
    _logger.debug("Debug message")
    _logger.info("Info message")
    _logger.warning("Warning message")
    _logger.error("Error message")
    _logger.critical("Critical message")


# Call main function
if __name__ == "__main__":
    sys.exit(main())
