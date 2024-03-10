from sqlalchemy import inspect

from phone_numbers_app.models import PhoneNumber


def test_fields(app):
    inspector = inspect(PhoneNumber)
    fields = [column.name for column in inspector.columns]
    print(fields)
    assert all(field in fields for field in ['id', 'phone']), (
        'В модели не найдены все необходимые поля. '
        'Проверьте модель: в ней должны быть поля id, и phone.'
    )
