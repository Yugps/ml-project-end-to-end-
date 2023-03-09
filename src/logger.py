import logging 
import os
from datetime import datetime 

log_file=f"{datetime.now().strftime('%m,%d,%Y,%H,%M,%S')}.log" # setting the format of the datetime that will appear on the log file name
log_path=os.path.join(os.getcwd(),'logs',log_file) # creating a default log path for making a directory
os.makedirs(log_path,exist_ok=True) # making a directory/folder to contain logs using the path created above 

log_file_path=os.path.join(log_path,log_file) # for basic config 

logging.basicConfig(filename=log_file_path,
                    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO)

if __name__=='__main__':
    logging.info('Logging has started') 
# execute above line to check if logger is working or not 




