from enum import StrEnum


class FieldTypes(StrEnum):
    EMAIL = "email"
    PHONE = "phone"
    DATE = "date"
    TEXT = "text"


FIELD_TEMPLATES = {
    "email": [r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+.[A-Za-z]{2,4}$"],
    "phone": [r"^\+7\s(\d{3})\s(\d{3})\s(\d{2})\s(\d{2})$"],
    "date": [
        r"^\d{4}-([0][1-9]|[1][1,2])-([0-2][0-9]|[3][0-1])$",
        r"^([0-2][0-9]|[3][0-1])-([0][1-9]|[1][1,2])-\d{4}$",
    ],
}
