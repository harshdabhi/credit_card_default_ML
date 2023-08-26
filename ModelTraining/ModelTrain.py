from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans # to select model for best categorisation
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression #since we have binary classification
import pandas as pd
import os
import pickle
import shutil
from kneed import KneeLocator



class model_training:


    def __init__(self) -> None:
        pass

    def test_cluster(self,X,Y):
        list_interia=[]
        for i in range(1,10):
            kmeans=KMeans(n_clusters=i)
            kmeans.fit(X,Y)
            list_interia.append(kmeans.inertia_)
        return list_interia


    def pre_model(self,dataframe):

        X=dataframe.drop('default',axis=1)
        Y=dataframe[['default']]

        sc=StandardScaler()  # save sc for transforming the user inputs
        os.makedirs('Models',exist_ok=True)

        pickle.dump(sc,file=open(f'StandardScalar.pkl','wb'))
        shutil.move(f'StandardScalar.pkl','Models')

        dfscaled=pd.DataFrame(sc.fit_transform(X),columns=X.columns)
        X=dfscaled

        kmeans=KMeans(n_clusters=10)
        kmeans.fit(X,Y)
        list_interia=[]
        for i in range(1,10):
            kmeans=KMeans(n_clusters=i)
            kmeans.fit(X,Y)
            list_interia.append(kmeans.inertia_)
        inertia_values=list_interia


        knee_value=KneeLocator(range(1,10),inertia_values,curve="convex",direction="decreasing")
        knee_value.plot_knee()
        elbow_value=knee_value.elbow # this will give us value to feed in kmeans
        
        km_model=KMeans(n_clusters=elbow_value)
        km_trained_model=km_model.fit(X,Y)
        pickle.dump(km_trained_model,file=open(f'kmeans.pkl','wb'))
        shutil.move(f'kmeans.pkl','Models')
        X['cluster']=km_trained_model.predict(X)
        df_final=X
        df_final['default']=Y
        return df_final,elbow_value

    
    def cluster_select(self,df,model,parameter,cluster_number,model_name):
        score_list=[]
        for i in range(0,cluster_number):
            x=df[df.cluster==i].drop(df.columns[-1:-3:-1],axis=1)
            y=df[df.cluster==i].default

            xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.3)
            G_model=GridSearchCV(estimator=model(),param_grid=parameter,cv=2)
            G_model.fit(xtrain,ytrain)
            best_parameters=G_model.best_params_
            model_=model(**best_parameters)
            model_train=model_.fit(xtrain,ytrain)
            scoring=model_train.score(xtest,ytest)
            score_list.append(scoring)
            pickle.dump(model_train,file=open(f'{model_name}_cluster{i}.pkl','wb'))
            os.makedirs('Models',exist_ok=True)
            shutil.move(f'{model_name}_cluster{i}.pkl','Models')
            
            print( f'{best_parameters} for cluster {i} and score {scoring}')
        return score_list
    
    
    def compare_lists(self,l1, l2):
        results = []
        for val1, val2 in zip(l1, l2):
            if val1 > val2:
                results.append(val1)
            else:
                results.append(val2)
        return results
    
    



    

    
    