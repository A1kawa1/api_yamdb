from datetime import date


def year_validate(data):
    if not (0 <= data <= date.today().year):
        raise ValueError('недопустимый год')