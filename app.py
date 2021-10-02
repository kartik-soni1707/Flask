import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from numpy import array


app = Flask(__name__)


@app.route('/')
def home(var1=0,var2=0):
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    
    '''
    with open("model.pkl", 'rb') as file:
        classifier = pickle.load(file)
    ans=[]
    for x in request.form.values():
        if x.isdigit():
            x=int(x)
        
        ans.append(x)
    value=ans

    value[0]=(value[0].lower()=='male')
    value[1]=(value[1].lower()=='yes')    
    value[3]=(value[3].lower()=='not grad')
    value[4]=(value[4].lower()=='yes')
    if(value[-1].lower()=='urban'):
        value[-1]=2
    elif(value[-1].lower()=='semiurban'):
        value[-1]=1
    else:
        value[-1]=0
    value=array(value, dtype=np.float64)
    res=classifier.predict([value,])

    output  = int(res[0][0])
    output="Eligible loan amount($) : "+ str(output)+str(value)
    return render_template('index.html', prediction_text=output)


if __name__ == "__main__":
    app.run(debug=True)
