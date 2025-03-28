from fastapi import FastAPI
from pydantic import BaseModel


# 데이터의 형식과 종류를 정의
class Item(BaseModel):
    name : str
    description : str | None = None
    price : float
    tax : float | None = None


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}