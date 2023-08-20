import shutil
import os
import re

class datasetvalidation:
    def __init__(self):
        pass
    
    def valid(self,dataset_path):
        st=os.listdir(dataset_path)
        for i in st:
            file=re.findall("[UCI_Credit_Card]+['']+[0-9]+['_']+[0-9]+['.']+[csv]",i)
            if file!=[]:
                for i in file:
                    os.makedirs('GoodDataSet',exist_ok=True)
                    shutil.copy(dataset_path+'/UCI_Credit_card_7879_9833','GoodDataSet')
            
            else:
                try:
                    os.makedirs('BadDataSet',exist_ok=True)
                    shutil.copy(dataset_path+'/'+i,'BadDataSet')
                except:
                    pass
