"""Integration tests for app.py"""
import pytest

from bank_api.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_account_creation(client):
    # Use the client to make requests e.g.:
    # client.post(...)
    # client.get(...)
    # https://flask.palletsprojects.com/en/1.1.x/testing/
    request = client.post('/accounts/test')
    assert request.status_code == 200
    assert request.json['name'] == 'test'

def test_account_retrieve(client):
    # Use the client to make requests e.g.:
    # client.post(...)
    # client.get(...)
    # https://flask.palletsprojects.com/en/1.1.x/testing/
    request = client.get('/accounts/test')
    assert request.status_code == 200
    assert request.json['name'] == 'test'
