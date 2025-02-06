import logging
import os
from datetime import datetime

# Get the project directory dynamically (where demo.py is located)
project_root = os.path.abspath(os.path.dirname(__file__))

# Define the logs directory inside the project
log_dir = os.path.join(project_root, "logs")

# Ensure the logs directory exists
os.makedirs(log_dir, exist_ok=True)

# Generate log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define full log file path inside the project
logs_path = os.path.join(log_dir, LOG_FILE)

# Set up logging configuration
logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

# Console logging (Optional: Prints logs to the terminal)
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s"))
logging.getLogger().addHandler(console_handler)
