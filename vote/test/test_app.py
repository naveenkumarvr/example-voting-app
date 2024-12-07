# tests/test_app.py
import pytest
from vote.app import app  # Adjust the import based on how the app is structured
import json


@pytest.fixture
def client():
    """Fixture to set up the Flask test client"""
    from vote.app import app
    app.testing = True
    client = app.test_client()
    yield client


def test_index(client):
    """Test the index route"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Vote for your favorite programming language!" in response.data


def test_vote_for_python(client):
    """Test voting for Python"""
    response = client.post('/vote', data={'lang': 'python'})
    assert response.status_code == 200
    assert b"Your vote for Python has been recorded!" in response.data


def test_vote_for_invalid_language(client):
    """Test voting with an invalid language"""
    response = client.post('/vote', data={'lang': 'ruby'})
    assert response.status_code == 400
    assert b"Invalid language" in response.data


def test_results(client):
    """Test the results page"""
    response = client.get('/results')
    assert response.status_code == 200
    # You can also check if the results contain the expected language names or vote counts
    assert b"Python" in response.data
    assert b"JavaScript" in response.data
