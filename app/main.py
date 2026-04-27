from fastapi import FastAPI
from app.auth.auth_api import auth_router

app = FastAPI()

app.include_router(auth_router,prefix="/auth ",tags=["login "])