from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.handlers import register_exception_handlers
from app.routes.admin import auth, staffs, meals
from app.core.logger import setup_logging

setup_logging()

app = FastAPI(root_path="/api")

register_exception_handlers(app)

origins = ["http://localhost:5173", "http://localhost"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router, prefix="/admin/auth")
app.include_router(staffs.router, prefix="/admin/staffs")
app.include_router(meals.router, prefix="/admin/meals")
