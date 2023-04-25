from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import pickle

model=pickle.load(open('PCASSS_model.pkl','rb'))
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('demo.html')

@app.route('/predict',methods=["POST"])
def predict1():
   
    input_features=[float(x) for x in request.form.values()]
    features_value=[np.array(input_features)]
    features_name=['Global_reactive_power','Global_intensity','Sub_metering_1','Sub_metering_2','Sub_metering_3']
    df=pd.DataFrame(features_value,columns=features_name)
    output=model.predict(df)
    
    return render_template('result1.html',prediction_text=output)

if __name__ == "__main__" :
        app.run(debug=True)