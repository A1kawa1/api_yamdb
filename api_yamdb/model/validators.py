from datetime import date


def year_validate(data):
    if not (0 <= data <= date.today()):
        raise ValueError('недопустимый год')