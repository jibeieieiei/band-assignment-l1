import requests
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


class Item(BaseModel):
    symbol: str  # Transaction symbol, e.g., BTC
    price: int  # Symbol price, e.g., 100000
    timestamp: int  # Timestamp of price retrieval


app = FastAPI()


@app.get("/get")
async def monitor(hash: str):
    api = f'https://mock-node-wgqbnxruha-as.a.run.app/check/{hash}'
    x = requests.get(api)
    return x.text


@app.post("/post")
async def broadcast(item: Item):
    api = 'https://mock-node-wgqbnxruha-as.a.run.app/broadcast'
    n_item = jsonable_encoder(item)
    x = requests.post(api, json=n_item)
    return x.text
