from flask import Flask,request,render_template
import pandas as pd
import numpy as np
import pickle as pk

from pyexpat import features

model=pk.load(open("model.pkl",'rb'))

#Flask app

app=Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predic():
    features=request.form['feature']
    featurs_list = [float(x.strip()) for x in features.split(",")]
    np_features=np.asarray(featurs_list,dtype=np.float32)
    pred=model.predict(np_features.reshape(1,-1))

    output=["Cancer" if pred[0]==1 else "Not Cancer"]
    return render_template('index.html',message=output)

#python main
if __name__=="__main__":
     app.run(debug=True)

