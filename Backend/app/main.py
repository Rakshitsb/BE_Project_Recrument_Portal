from fastapi import FastAPI
from app.routers import auth, admin, hr, user

app = FastAPI()

app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(hr.router)
app.include_router(user.router)
