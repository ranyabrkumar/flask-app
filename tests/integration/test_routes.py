import pytest
from flask import Flask

@pytest.fixture
def app():
    app = Flask(__name__)

    @app.route('/ping', methods=['GET'])
    def ping():
        return "pong", 200

    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_ping_route(client):
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "pong"