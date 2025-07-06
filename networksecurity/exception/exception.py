# (d:\Udemy\Complete_DSMLDLNLP_Bootcamp\Python\49-End To End MLOPS Project with ETL Pipelines\venv) 
# D:\Udemy\Complete_DSMLDLNLP_Bootcamp\Python\49-End To End MLOPS Project with ETL Pipelines\networksecurity\exception>
# python exception.py

from networksecurity.logging import logger
import sys

class NetworkSecurityException(Exception):
    def __init__(self, error, error_message:sys):
        self.error = error
        _,_,exc_tb = error_message.exc_info()

        self.line_no = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error '{str(self.error)}' has occured. It is in line number {self.line_no} of file {self.file_name}"
    
if __name__ == "__main__":
    try:
        logger.logging.info("Division by zero error in exception.py")
        a = 1/0
    except Exception as e:
        raise NetworkSecurityException(e, sys)

# module>
#    raise NetworSecurityException(e, sys)
#__main__.NetworSecurityException: Error 'division by zero' has occured. It is in line number 17 of file D:\Udemy\Complete_DSMLDLNLP_Bootcamp\Python\49-End To End MLOPS Project with ETL Pipelines\networksecurity\exception\exception.py