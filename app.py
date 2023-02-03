import uvicorn
from fastapi import FastAPI
import numpy as np
import pickle
import pandas as pd
from price_info import PriceInfo

app = FastAPI()
pkl_in = open("nas100.pkl", 'rb')
classifier=pickle.load(pkl_in)


@app.get('/')
def index():
    return {'message': 'Hello Thabang'}

@app.get('/{name}')
def get_name(name: str):
    return {'message': f'Weclome back Sir,{name}'}


@app.post('/predict')
def pred_price(data:PriceInfo):
    data = data.dict()
    open=data['open']
    volume=data['volume']
    low=data['low']
    high=data['high']
    inpt_val = (open,volume,low,high)
    input_dt = np.asarray(inpt_val)
    reshape_vals = input_dt.reshape(1, -1)
    anticipated = classifier.predict(reshape_vals)
    if (inpt_val[0] < anticipated):
        anticipated = f"Buy!! & TP:{anticipated.round(2)}"
    else:
        anticipated = f"Sell!! & TP:{anticipated.round(2)}"
    return {"prediction": anticipated}
    
@app.get('/prediction')
def get_cat(open: float, volume: float, low: float, high: float):
    anticipated = classifier.predict([[open, volume, low, high]])
    return {'prediction': anticipated}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
