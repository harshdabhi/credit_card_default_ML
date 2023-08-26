from flask import Flask,render_template,request

app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def homepage():
    return render_template('home.html')

@app.route('/predict',method=['POST'])
def prediction():
    return render_template('predict.html')


if __name__=='__main__':
    app.run(debug=True)