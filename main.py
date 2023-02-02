'''
@rttteddy.gmail.com
'''
import uvicorn
from fastapi import FastAPI

# The app object
app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello Thabang'}

@app.get('/Welcome')
def get_name(name: str):
    return{"Welcome to your first API": f'{name}'}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
#uvicorn main:app --reload