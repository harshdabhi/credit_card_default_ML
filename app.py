from flask import Flask,render_template,request
import json
import numpy as np
import pickle

app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def homepage():
    return render_template('home.html')

@app.route('/predict',method=['POST'])
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
            BILL_AMT1 =request.form['bill_amt1']
            BILL_AMT2 =request.form['bill_amt2']
            BILL_AMT3 =request.form['bill_amt3']
            BILL_AMT4 =request.form['bill_amt4']
            BILL_AMT5 =request.form['bill_amt5']
            BILL_AMT6 =request.form['bill_amt6']
            PAY_AMT1 =request.form['pay_amt1']
            PAY_AMT2 =request.form['pay_amt2']
            PAY_AMT3 =request.form['pay_amt3']
            PAY_AMT4 =request.form['pay_amt4']
            PAY_AMT5 =request.form['pay_amt5']
            PAY_AMT6 =request.form['pay_amt6']
            LIMIT_AMT=request.form['limit_amount']

            val=np.array((LIMIT_AMT,SEX,EDUCATION,MARRIAGE,AGE,PAY_1,PAY_2,PAY_3,PAY_4,PAY_5,PAY_6,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6)).reshape(1,-1)
            sc=pickle.load(open('Models/StandardScalar.pkl','rb'))
            val=sc.transform(val)

            f=pickle.load(open('Models/kmeans.pkl','rb'))
            cluster_number=f.predict(val)


            with open("data.json", "r") as json_file:
                loaded_data = json.load(json_file)

            loaded_dict = dict(loaded_data)
            model_file=loaded_dict[cluster_number[0]]

            pred=pickle.load(open(f'Models/{model_file}','rb'))
            prediction_value=pred.predict(val)

            if prediction_value==0:
                content={'display':'Less possibility of default'}
            
            if prediction_value==1:
                content={'display':'case of credit card payment default is likely'}



    return render_template('predict.html',context=content)


if __name__=='__main__':
    app.run(debug=True)