from fastapi import FastAPI
from app.database import engine
from app import models

app = FastAPI()

models.Base.metadata.create_all(engine)


@app.get('/')
def test():
    return {"message": "Testing Successful"}