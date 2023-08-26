
from pymongo import MongoClient
import json
import pandas as pd
import os
from configparser import ConfigParser
from logger import logging

os.path.join('./GoodDataSet')


class datatrans:
    '''
    
    
    
    '''

    def __init__(self) -> None:
        pass

    def mongoDB(self):

        try:

            user=ConfigParser()
            user.read('config.ini')

        
            client = MongoClient(f'mongodb+srv://test:{user["mongoDB"]["pass"]}@clustercreditcard.zoinfjf.mongodb.net/?retryWrites=true&w=majority')
    
            db=client['databases']
            collections=db['GoodDataCollection']
            
            for i in os.listdir('./GoodDataSet'):
                file=pd.read_csv('./GoodDataSet/'+i)
                os.makedirs('./GoodDataSet/Json_file',exist_ok=True)
                file.to_json('./GoodDataSet/Json_file/'+i.split('.')[0]+'.json')
                with open('./GoodDataSet/Json_file/'+i.split('.')[0]+'.json') as f:
                    data=json.load(f)
                collections.insert_one(data)
                print('data inserted')
                logging.info('Data has been inserted into databases')
                data.close()
                
            client.close()


        

        except:
            pass
