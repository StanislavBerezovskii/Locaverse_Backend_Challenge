import pytest

from phone_numbers_app import create_app, db


@pytest.fixture()
def app():
    """Sets up temporary testing app and database"""
    app = create_app("sqlite://")

    with app.app_context():
        db.create_all()

    yield app


@pytest.fixture()
def client(app):
    """Sets up app client"""
    return app.test_client()
