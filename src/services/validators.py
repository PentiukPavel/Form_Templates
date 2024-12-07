import re

from core.database import db
from services.templates import FIELD_TEMPLATES, FieldTypes


def define_type_of_value(value: str) -> str:
    """
    Функция для определения типа поля
    :param value: значение
    """

    for template in list(sorted(FIELD_TEMPLATES.keys())):
        for i in FIELD_TEMPLATES[template]:
            if re.match(i, value):
                return template
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
    all_templates = db.all()
    for template in all_templates:
        temp_keys = set(template)
        temp_keys.remove("name")
        if form_keys >= temp_keys:
            for k in temp_keys:
                print(k, form[k], template[k])
                if not form[k] == template[k]:
                    break
            return {"name": template["name"]}
    return form
