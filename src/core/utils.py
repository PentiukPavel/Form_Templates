from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.database import db
from mock_data.data import TEST_DATA


@asynccontextmanager
async def lifespan(app: FastAPI):
    if len(db.all()) == 0:
        for form in TEST_DATA:
            db.insert(form)
    yield
