import requests
import os
import pytest

BASE_URL = os.getenv('BASE_URL', 'http://localhost:5000')

def is_server_running():
    """Check if the server is running before running E2E tests."""
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=2)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

@pytest.mark.skipif(not is_server_running(), reason="Flask server not running on localhost:5000")
def test_hello_world_e2e():
    """Test the hello_world route in an end-to-end manner."""
    res = requests.get(f"{BASE_URL}/")
    assert res.status_code == 200
    data = res.json()
    assert data['message'] == 'Python Flask App created by Optimum IDP!'
    assert data['status'] == 'success'

@pytest.mark.skipif(not is_server_running(), reason="Flask server not running on localhost:5000")
def test_health_check_e2e():
    """Test the health check endpoint in an end-to-end manner."""
    res = requests.get(f"{BASE_URL}/health")
    assert res.status_code == 200
    data = res.json()
    assert data['status'] == 'healthy'
