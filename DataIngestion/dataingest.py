import pandas as pd
from logger import logging

class dataingest:
    def __init__(self) -> None:
        pass

    def load_data_local(self,file_path):
        try:
            data=pd.read_csv(file_path)
            logging.info('data has been fetch from final data sets ')
            return data
        except Exception as e:
            pass

    
    