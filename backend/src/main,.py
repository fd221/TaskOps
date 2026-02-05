from fastapi import FastAPI

from db import engine
from src.auth.router import router_db
from src.auth.models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router_db)