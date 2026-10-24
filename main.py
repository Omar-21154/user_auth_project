from fastapi import FastAPI

from database import Base, engine
from user_model import User
from routers import auth, users

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
