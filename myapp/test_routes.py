import pytest
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_health_check(client):
    res = client.get('/health')
    assert res.status_code == 200
    assert res.json['status'] == 'healthy'
    assert res.content_type == 'application/json'

def test_greet(client):
    name = 'Abhimanyu'
    res = client.get(f'/greet/{name}')
    assert res.status_code == 200
    assert res.json['message'] == f'Hello, {name}! Welcome to Flask starter app.'
    assert res.content_type == 'application/json'
