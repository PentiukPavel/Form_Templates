import re

from core.database import db
from validation.templates import FIELD_TEMPLATES, FieldTypes


def define_type_of_value(value: str) -> str:
    """
    Функция для определения типа поля
    :param value: значение
    """

    for temp in list(sorted(FIELD_TEMPLATES.keys())):
        for i in FIELD_TEMPLATES[temp]:
            if re.match(i, value):
                return temp
    return FieldTypes.TEXT.value


def define_type_of_form_fields(form: dict) -> dict:
    """
    Функция для типов полей формы
    :param form: форма
    :return: словарь с типовыми значаниями данных из FieldTypes
    """

    form_types = {}
    for field in form:
        form_types[field] = define_type_of_value(str(form[field]))
    return form_types


def find_form(form: dict) -> dict:
    """
    Функция для поиска нужного шаблона для формы
    :param form: форма
    :return: название найденного в БД шаблона или шаблон для входящей формы
    """

    form = define_type_of_form_fields(form)
    form_keys = set(form)
    existing_forms = db.all()
    for ef in existing_forms:
        ef_keys = set(ef)
        ef_keys.remove("name")
        if form_keys >= ef_keys:
            for i in ef_keys:
                print(i, form[i], ef[i])
                if not form[i] == ef[i]:
                    break
            return {"name": ef["name"]}
    return form
