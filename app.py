from flask import Flask,render_template,request
import json
import numpy as np
import pickle
from DataPreprocessing.preprocess import preprocess
import pandas as pd

app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def homepage():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def prediction():
    if request.method=='POST':
            SEX =request.form['sex']
            EDUCATION=request.form['education']
            MARRIAGE=request.form['marriage']
            AGE =request.form['age']
            PAY_1 =request.form['pay_1']
            PAY_2 =request.form['pay_2']
            PAY_3 =request.form['pay_3']
            PAY_4 =request.form['pay_4']
            PAY_5 =request.form['pay_5']
            PAY_6 =request.form['pay_6']
            BILL_AMT1 =request.form['bill_amount1']
            BILL_AMT2 =request.form['bill_amount2']
            BILL_AMT3 =request.form['bill_amount3']
            BILL_AMT4 =request.form['bill_amount4']
            BILL_AMT5 =request.form['bill_amount5']
            BILL_AMT6 =request.form['bill_amount6']
            PAY_AMT1 =request.form['pay_amount1']
            PAY_AMT2 =request.form['pay_amount2']
            PAY_AMT3 =request.form['pay_amount3']
            PAY_AMT4 =request.form['pay_amount4']
            PAY_AMT5 =request.form['pay_amount5']
            PAY_AMT6 =request.form['pay_amount6']
            LIMIT_AMT=request.form['limit_amount']
 
            val=np.array((LIMIT_AMT,SEX,EDUCATION,MARRIAGE,AGE,PAY_1,PAY_2,PAY_3,PAY_4,PAY_5,PAY_6,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6)).reshape(1,-1)
            p_=preprocess()
            sc=p_.scalar_standard(pd.read_csv('./FinalDataSet/UCI_Credit_Card.csv'))
            val=sc.transform(val)

            f=pickle.load(open('Models/kmeans.pkl','rb'))
            cluster_number=f.predict(val)


            with open("data.json", "r") as json_file:
                loaded_data = json.load(json_file)

            loaded_dict = dict(loaded_data)
            print(loaded_dict)
            model_file=loaded_dict[str(cluster_number[0])]

            pred=pickle.load(open(f'Models/{model_file}','rb'))
            prediction_value=pred.predict(val)

            if prediction_value==0:
                content='credit card default is not possible'
            
            elif prediction_value==1:
                content='credit card payment default is possible'



    return render_template('predict.html',data=content)


if __name__=='__main__':
    app.run(host ='0.0.0.0', port = 5001,debug=True)
