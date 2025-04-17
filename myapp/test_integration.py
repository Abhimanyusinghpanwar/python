import logging
import pytest
from main import app

@pytest.fixture
def test_app():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_route_logging(caplog, test_app):
    with caplog.at_level(logging.DEBUG):
        res = test_app.get('/health')
        assert res.status_code == 200
        assert 'Health check endpoint called' in caplog.text

def test_greet_route_logging(caplog, test_app):
    with caplog.at_level(logging.INFO):
        res = test_app.get('/greet/IntegrationTest')
        assert res.status_code == 200
        assert res.json['message'] == "Hello, IntegrationTest! Welcome to Flask starter app."
        assert 'Greet endpoint called with name: IntegrationTest' in caplog.text