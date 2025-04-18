import logging
import pytest
from app import app

@pytest.fixture
def test_app():
    """Fixture to create a test client for integration tests."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world_logging(caplog, test_app):
    """Test the hello_world route with logging."""
    with caplog.at_level(logging.DEBUG):
        res = test_app.get('/')
        assert res.status_code == 200
        assert 'Hello World endpoint called' in caplog.text

def test_health_route_logging(caplog, test_app):
    """Test the /health route with logging."""
    with caplog.at_level(logging.DEBUG):
        res = test_app.get('/health')
        assert res.status_code == 200
        assert 'Health check endpoint called' in caplog.text