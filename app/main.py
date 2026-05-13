from fastapi import Depends, FastAPI
from app.auth.auth_dependency import admin_required, user_required
from app.router.auth_api import auth_router
from app.router.user_api import user_router
from app.router.admin_api import admin_router
from app.db.database import engine, Base

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


app.include_router(auth_router,tags=["login "])
app.include_router(user_router,tags=["user"],dependencies=[Depends(user_required)])
app.include_router(admin_router,tags=["admin"],dependencies=[Depends(admin_required)])
    