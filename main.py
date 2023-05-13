# from fastapi import FastAPI
from flask import Flask, request 
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('./data/diagnoses2019.csv')

@app.route('/', methods=["GET"])
def home():
    return 'this is the home page'

@app.route('/preview', methods=["GET"])
def preview():
    return df.head()

if __name__ == '__main__':
    app.run(debug=True)

# app = FastAPI()
# @app.get("/")
# async def root():
#     return 'hello' 