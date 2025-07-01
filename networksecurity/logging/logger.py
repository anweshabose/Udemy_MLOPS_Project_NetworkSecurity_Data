# (d:\Udemy\Complete_DSMLDLNLP_Bootcamp\Python\49-End To End MLOPS Project with ETL Pipelines\venv) 
# D:\Udemy\Complete_DSMLDLNLP_Bootcamp\Python\49-End To End MLOPS Project with ETL Pipelines\networksecurity\logging>
# python logger.py

from datetime import datetime
import os
import logging

log_file = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}"
log_path = os.path.join(os.getcwd(), "logs", log_file)
os.makedirs(log_path, exist_ok=True)

log_file_path = os.path.join(log_path,log_file)

logging.basicConfig(filename=log_file_path, level=logging.INFO, format="%(asctime)s - %(lineno)d - %(levelname)s - %(message)s")

if __name__ == "__main__":
    logging.info("Successfully Initialized the logging.py file")

# D:\Udemy\Complete_DSMLDLNLP_Bootcamp\Python\49-End To End MLOPS Project with ETL Pipelines\networksecurity\logging\logs\01_07_2025_22_20_27
# 2025-07-01 22:20:27,029 - 16 - INFO - Successfully Initialized the logging.py file