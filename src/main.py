from contextlib import asynccontextmanager
from fastapi import FastAPI
from logs.log_middleware import LoggingMiddleware

from api.routers import v1_main_router
from core.database import db


@asynccontextmanager
async def lifespan(app: FastAPI):
    db.insert(
        {
            "name": "MyForm",
            "employee_phone": "phone",
            "employee_email": "email",
            "birth_date": "date",
        }
    )
    yield


app = FastAPI(
    lifespan=lifespan,
    title="API",
    summary="API",
)
app.middleware("http")(LoggingMiddleware())


app.include_router(v1_main_router)
