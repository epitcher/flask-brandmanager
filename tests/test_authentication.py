import pytest
from app import create_app
from .utils import login, logout

valid_username = "user"
valid_password = "user"
invalid_username = "invalid"
invalid_password = "invalid"

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

# Test login page
def test_login_get(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Login' in response.data

# Test valid login credentials
def test_login_post_valid_credentials(client):
    response = login(client, valid_username, valid_password)
    assert response.status_code == 200
    assert b'Home' in response.data

# Test invalid login credentials
def test_login_post_invalid_credentials(client):
    response = login(client, invalid_username, invalid_password)
    assert response.status_code == 401

# Test logout functionality
def test_logout(client):
    # Log in with valid credentials
    login_response = login(client, valid_username, valid_password)
    assert b'Home' in login_response.data

    # Log out
    logout_response = logout(client)
    assert logout_response.status_code == 200
    assert b'Logged out successfully' in logout_response.data
    assert b'Login' in logout_response.data
