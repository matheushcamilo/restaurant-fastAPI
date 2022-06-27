from fastapi import FastAPI
from .database import engine, Base
from .routers import client, order, authentication

app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(client.router)
app.include_router(order.router)
app.include_router(authentication.router)
