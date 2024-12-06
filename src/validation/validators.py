import re

from core.database import db
from validation.templates import FIELD_TEMPLATES, FieldTypes


def define_type_of_value(value) -> str:
    for temp in list(sorted(FIELD_TEMPLATES.keys())):
        for i in FIELD_TEMPLATES[temp]:
            if re.match(i, value):
                return temp
    return FieldTypes.TEXT.value


def define_type_of_form_fields(form: dict) -> dict:
    form_types = {}
    for field in form:
        form_types[field] = define_type_of_value(form[field])
    return form_types


def find_form(form: dict):
    form = define_type_of_form_fields(form)
    form_keys = set(form)
    existing_forms = db.all()
    for ef in existing_forms:
        ef_keys = set(ef)
        ef_keys.remove("name")
        if form_keys >= ef_keys:
            for i in ef_keys:
                if not form[i] == ef[i]:
                    break
            return ef
    return form
