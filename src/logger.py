import logging
import os
from datetime import datetime

LOG_FILE_NAME = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
logs_folder_path = os.path.join(os.getcwd(),"logs",LOG_FILE_NAME)

os.makedirs(logs_folder_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_folder_path,LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)