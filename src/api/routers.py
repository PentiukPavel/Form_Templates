from fastapi import APIRouter

from api.endpoints import v1_forms_router


v1_main_router = APIRouter()

v1_main_router.include_router(v1_forms_router)
