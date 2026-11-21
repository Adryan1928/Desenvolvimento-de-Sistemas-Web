from datetime import datetime
from django.core.exceptions import ValidationError


def validate_ano_publicacao(value):
    year = datetime.now().year
    if value < 1450 or value > year:
        raise ValidationError(f"A data não corresponde ao range de 1450 á {year}.")


def validate_paginas(value):
    if value < 1 or value > 5000:
        raise ValidationError(f"A quantidade de páginas não corresponde ao range de 1 á 5000.")


def validate_isbn(value):
    if len(value) != 13:
        raise ValidationError("ISBN deve ter exatamente 13 dígitos.")
    