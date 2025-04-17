import requests
import os
import pytest

BASE_URL = os.getenv('BASE_URL', 'http://localhost:5000')

def test_health_check_e2e():
    try:
        res = requests.get(f"{BASE_URL}/health")
        res.raise_for_status()
        assert res.status_code == 200
        assert res.json()['status'] == 'healthy'
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Health check failed: {e}")

def test_greet_e2e():
    name = "TestUser"
    try:
        res = requests.get(f"{BASE_URL}/greet/{name}")
        res.raise_for_status()
        assert res.status_code == 200
        assert res.json()['message'] == f"Hello, {name}! Welcome to Flask starter app."
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Greet endpoint failed: {e}")