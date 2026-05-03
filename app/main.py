from fastapi import FastAPI
from app.auth.auth_api import auth_router
from app.db.database import engine, Base


app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

    
app.include_router(auth_router,prefix="/auth ",tags=["login "])
