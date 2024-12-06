from pydantic import BaseModel


class FormName(BaseModel):
    name: str
