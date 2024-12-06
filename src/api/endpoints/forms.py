from fastapi import APIRouter, Body

from validation.validators import find_form


v1_forms_router = APIRouter(prefix="/api/v1", tags=["Forms"])


@v1_forms_router.post("/get_form")
async def get_form_endpoint(
    form: dict = Body(
        ...,
        examples=[
            {
                "employee_phone": "+7 000 000 00 00",
                "employee_email": "example@example.org",
                "birth_date": "2024-01-01",
            },
        ],
    )
):
    return find_form(form)
