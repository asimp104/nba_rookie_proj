import flask
from flask import Flask, jsonify, request
import json
import pickle
import numpy as np
import pandas as pd

def load_models():
    file_name1 = 'models/model_file.p'
    file_name2 = 'models/transform_file.p'
    
    with open(file_name1, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
        
    with open(file_name2, 'rb') as pickled:
        data = pickle.load(pickled)
        transform = data['transform']    
    return model, transform

app = Flask(__name__)
@app.route('/predict', methods=['GET'])

def predict():
    model, transform = load_models()
    request_json = request.get_json()
    x = request_json['input']
    x_in = pd.DataFrame(columns =  [i for i in range(len(x))])
    x_in.loc[0] = x
    
    x_in = transform.transform(x_in)
    
    prediction = int(model.predict(x_in)[0])
    response = json.dumps({'response': prediction})
    return response, 200

if __name__ ==  '__main__':
    application.run(debug=True)