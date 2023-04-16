from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import user, dogs

app = FastAPI(
    title="WOOF MATES API"
)
app.include_router(user.router)
app.include_router(dogs.router)

models.Base.metadata.create_all(engine)
