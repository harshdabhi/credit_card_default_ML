from logger import logging
from sklearn.preprocessing import StandardScaler

class preprocess:
    def __init__(self) -> None:
        pass


    def data_imputation(self,dataframe):
        '''
        This function is to fill na value with mean of data sets 
        
        '''
        df=dataframe
        c=df[df.isnull()].count()

        for i in range(len(c.keys())):
            if c[i]!=0:
                df[c.keys()[i]].fillna(df[c.keys()[i]].mean())
                logging.info(f'Data has been imputed for column {c.keys()[i]}')
                
        return df


    # we need to now clean the data sets 

    # change the clean the data of education columns
    # Education range from : (1 = graduate school; 2 = university; 3 = high school; 4 = others).
    # so any inputs beyond 3 falls in other categorgy unlike giving input ay=t max 6

    def clean_education(self,number):
        if number>=4:
            data=4
        else:
            data=number
        return data 


    def rename_col(self,dataframe,old_name,new_name):
        dataframe.rename({old_name:new_name},axis=1,inplace=True)


    # we are intreset who didnt pay the payments so if anyone pay must be replace by 0 and didnt pay will be number from 1 to 4

    def pay_duly(self,number):
        if number<0:
            return 0
        else:
            return number
        

    def quick_clean(self,dataframe):
        '''
        This function will clean and fix the datasets with proper conventions 
        '''
        dataframe['EDUCATION']=dataframe['EDUCATION'].apply(self.clean_education)
        self.rename_col(dataframe,'PAY_0','PAY_1')
        self.rename_col(dataframe,'default.payment.next.month','default')

        for i in range(1,7):
            dataframe[f'PAY_{i}']=eval(f'dataframe.PAY_{i}.apply(self.pay_duly)')
        
        #dropping id column as every customer data has its own unique id
        dataframe.drop('ID',axis=1,inplace=True)

        logging.info('dataimputation has been completed')
        return dataframe
    
    def scalar_standard(self,dataframe):
        X=dataframe.drop('default.payment.next.month',axis=1)
        X=X.drop('ID',axis=1)

        sc=StandardScaler()
        sc.fit_transform(X)
        return sc

    
