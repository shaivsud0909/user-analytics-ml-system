from fastapi import FastAPI
from app.router.auth_api import auth_router
from app.router.model_api import user_router
from app.router.admin_api import admin_router
from app.db.database import engine, Base

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

    
app.include_router(auth_router,tags=["login "])
app.include_router(user_router,tags=["user"])
app.include_router(admin_router,tags=["admin"])
