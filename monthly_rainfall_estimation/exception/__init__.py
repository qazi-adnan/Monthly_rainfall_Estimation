import os
import sys
import logging
from datetime import datetime

# Get the project directory dynamically (where this script is located)
project_root = os.path.abspath(os.path.dirname(__file__))

# Define logs directory inside the project
log_dir = os.path.join(project_root, "logs")

# Ensure the logs directory exists
os.makedirs(log_dir, exist_ok=True)

# Define the error log file path
error_log_file = os.path.join(log_dir, "exceptions.log")

# Configure logging to save errors in a file
logging.basicConfig(
    filename=error_log_file,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.ERROR,
)

# Also log errors to the console
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s"))
logging.getLogger().addHandler(console_handler)

def error_message_detail(error, error_detail: sys):
    """
    Extracts detailed error message with script name, line number, and error description.

    :param error: Exception instance
    :param error_detail: sys module for error traceback details
    :return: Formatted error message string
    """
    exc_type, exc_value, exc_tb = error_detail.exc_info()

    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
    else:
        file_name = "Unknown"
        line_number = "Unknown"

    error_message = f"Error occurred in script: [{file_name}], Line: [{line_number}], Message: [{str(error)}]"

    # Save error to log file
    logging.error(error_message)

    return error_message

class RainfallException(Exception):
    """
    Custom Exception Class for handling errors in the Rainfall Estimation project.
    """
    def __init__(self, error_message, error_detail: sys):
        """
        Initializes the custom exception with a detailed error message.

        :param error_message: Error message string
        :param error_detail: sys module for traceback details
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
