import requests
import os
import pytest

BASE_URL = os.getenv('BASE_URL', 'http://localhost:5000')

def test_hello_world_e2e():
    """Test the hello_world route in an end-to-end manner."""
    try:
        res = requests.get(f"{BASE_URL}/")
        res.raise_for_status()
        assert res.status_code == 200
        assert res.json()['message'] == 'Python Flask App created by Optimum IDP!'
        assert res.json()['status'] == 'success'
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Hello World endpoint failed: {e}")

def test_health_check_e2e():
    """Test the health check endpoint in an end-to-end manner."""
    try:
        res = requests.get(f"{BASE_URL}/health")
        res.raise_for_status()
        assert res.status_code == 200
        assert res.json()['status'] == 'healthy'
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Health check failed: {e}")