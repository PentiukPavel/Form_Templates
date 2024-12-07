from fastapi import APIRouter, Body

from services.validators import find_form
from schemes import FormName


v1_forms_router = APIRouter(prefix="/api/v1", tags=["Forms"])


@v1_forms_router.post(
    "/get_form",
    summary="Получение названия формы.",
    description=(
        "Получение формы шаблона или, при отсутствии шаблона "
        "в базе, списка типов полей отправленной формы."
    ),
    response_model_include=FormName,
)
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
