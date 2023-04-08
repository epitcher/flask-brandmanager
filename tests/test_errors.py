import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

## Test Errors ##

# Test 404 error page
def test_404_page(client):
    response = client.get('/nonexistent_route')
    assert response.status_code == 404
    assert b'404' in response.data # Expand?
