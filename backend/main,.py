from fastapi import FastAPI
from router import router_db

from db import engine
from models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router_db)