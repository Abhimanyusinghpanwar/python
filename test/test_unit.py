"""Tests for the Python Flask app."""
import json
import pytest
from app import app
 
 
@pytest.fixture
def client():  # pylint: disable=redefined-outer-name
    """Create a test client for the app."""
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        yield test_client
 
 
def test_hello_world_route(client):  # pylint: disable=redefined-outer-name
    """Test the hello_world route returns the expected response."""
    response = client.get('/')
 
    # Check status code
    assert response.status_code == 200
 
    # Parse response data
    data = json.loads(response.data.decode('utf-8'))
 
    # Check response structure
    assert 'message' in data
    assert 'status' in data
 
    # Check response content
    assert data['message'] == 'Python Flask App created by Optimum IDP!'
    assert data['status'] == 'success'
 
 
def test_health_check_route(client):  # pylint: disable=redefined-outer-name
    """Test the health_check route returns a healthy status."""
    response = client.get('/health')
 
    # Check status code
    assert response.status_code == 200
 
    # Parse response data
    data = json.loads(response.data.decode('utf-8'))
 
    # Check response structure and content
    assert 'status' in data
    assert data['status'] == 'healthy'