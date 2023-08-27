from DataIngestion.DataIngest import dataingest
from DataPreprocessing.preprocess import preprocess
from ModelTraining.ModelTrain import model_training
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression 
import json
#since we have binary classification


class predict:
    def __init__(self) -> None:
        pass

    def prediction(self):

        df=dataingest()
        df=df.load_data_local('./FinalDataSet/UCI_Credit_Card.csv')

        p=preprocess()
        df=p.data_imputation(df)
        df=p.quick_clean(df)

        m=model_training()
        df,elbow_value=m.pre_model(df)


        m1=m.cluster_select(df,LogisticRegression,{'penalty':['l1','l2','elasticnet'],'solver':['lbfgs','liblinear','newton-cg','newton-cholesky','sag','saga']},elbow_value,'logisticR')
        m2=m.cluster_select(df,RandomForestClassifier,{'criterion':['gini','entropy','log_loss'],'max_features':['sqrt','log2'],'max_depth':range(2,8)},elbow_value,'randomF')

        best_performing_model=m.compare_lists(m1,m2)

        dict1={}

        for count1,i in enumerate(best_performing_model):
        
            if i in m1:
                dict1[count1]=f'logisticR_cluster{count1}.pkl'
            elif i in m2:
                dict1[count1]=f'randomF_cluster{count1}.pkl'


        json_data = json.dumps(dict1)

        with open("data.json", "w") as json_file:
            json_file.write(json_data)

        
        return dict1


if __name__=="__main__":

    f=predict()
    c=f.prediction()
    

