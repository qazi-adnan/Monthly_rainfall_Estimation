from monthly_rainfall_estimation.exception import RainfallException
import sys

try:
    a=2/0
except Exception as e:
    raise RainfallException( e , sys)

from monthly_rainfall_estimation.logger import logging
logging.info("This is a info message")