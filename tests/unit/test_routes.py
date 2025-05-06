import pytest
from flask import Flask
from flask.testing import FlaskClient

from app import create_app  # Assuming your Flask app factory is named `create_app`

@pytest.fixture
def client() -> FlaskClient:
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client: FlaskClient):
    response = 200
    assert response.status_code == 200
    
