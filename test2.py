import numpy as np
from flask import Flask, jsonify, request, render_template
from array import *

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    import requests
    '''
    For rendering results on HTML page
    '''
    fl_features = [str(x) for x in request.form.values()]
    payload="{\"data\":ftldata}"
    url = "https://6l6l7n7vtb.execute-api.us-east-2.amazonaws.com/test/predict"

    #payload="{\"data\":\"0,-0.34147611300851444,0.18202662446267728,310000.0,2.0,2.0,1.0,44.0,-1.0,-1.0,-2.0,-2.0,-2.0,-2.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0\"}"
    headers = {'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data=payload)
    name = str(response.text)
    #return render_template('index.html', prediction_text=name)
    return render_template('index.html', prediction_text=fl_features)
	
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port='8080')




