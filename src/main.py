from fastapi import FastAPI
from logs.log_middleware import LoggingMiddleware

from api.routers import v1_main_router
from core.utils import lifespan


app = FastAPI(
    lifespan=lifespan,
    title="API",
    summary="API",
)
app.middleware("http")(LoggingMiddleware())


app.include_router(v1_main_router)
