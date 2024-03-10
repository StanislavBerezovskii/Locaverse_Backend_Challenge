from sqlalchemy import inspect

from phone_numbers_app.models import PhoneNumber


def test_fields(app):
    """Testing the database for essential fields"""
    inspector = inspect(PhoneNumber)
    fields = [column.name for column in inspector.columns]
    print(fields)
    assert all(field in fields for field in ['id', 'phone']), (
        'The model is missing essential fields. '
        'Check model: it must contain id, and phone fields.'
    )
