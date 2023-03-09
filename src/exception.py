import sys 
import logging 
import logger

def error_message_handler(error,error_details:sys): # here sys means that error_details will be a variabe of sys type
    _,_,exc_tb=error_details.exc_info() # This basically gives exceution info provides 3 values , we are interested in the last one 
    file_name=exc_tb.tb_frame.f_code.co_filename # we are tyring to get file name here 
    error_message=f"error occured in script name {file_name} line_number {exc_tb.tb_lineno} error message {error}"
    return error_message


# we created the class below to call the above function and get the complete error message 
class custom_exception(Exception):
    def __init__(self,error_message,error_detail:sys): # here sys means that error_details will be a variabe of sys type
        super().__init__(error_message)
        self.error_message=error_message_handler(error_message,error_details=error_detail)

    def __str__(self):
        return self.error_message
    

try:
    a=1/0
except Exception as e:
    logging.info('Divide by zero error')
    raise custom_exception(e,sys)