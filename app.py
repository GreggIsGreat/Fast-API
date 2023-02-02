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
    prediction = classifier.predict(reshape_vals)
    if (inpt_val[0] < prediction):
        prediction = f"Buy!! & TP:{prediction.round(2)}"
    else:
        prediction = f"Sell!! & TP:{prediction.round(2)}"
    return {
        "prediction": prediction
    }

    

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
