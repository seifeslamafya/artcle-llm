# logger_config.py
import logging

# Configure logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler("app.log", mode="a")
file_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(client_ip)s - %(func_name)s - %(status_code)s - %(message)s"
)
file_handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(file_handler)
