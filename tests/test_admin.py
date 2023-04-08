import pytest
from app import create_app
from .utils import login, logout, valid_username, valid_password

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


## Test module/admin ##

# Test /account page access for non-logged-in users
def test_admin_analytics_access_non_logged_in_user(client):
    response = client.get('/analytics', follow_redirects=True)
    assert response.status_code == 200
    assert b'Login' in response.data

# Test /account page access for logged-in users
def test_admin_analytics_access_logged_in_user(client):
    # Use login utility
    login(client, valid_username, valid_password)

    # Access the /account page
    account_response = client.get('/analytics', follow_redirects=True)
    assert account_response.status_code == 200
    assert b'analytics' in account_response.data

    # Log out
    logout(client)

# Test /search page access for non-logged-in users
def test_admin_upload_access_non_logged_in_user(client):
    response = client.get('/upload', follow_redirects=True)
    assert response.status_code == 200
    assert b'Login' in response.data

# Test /search page access for logged-in users
def test_admin_upload_access_logged_in_user(client):
    login(client, valid_username, valid_password)

    search_response = client.get('/upload', follow_redirects=True)
    assert search_response.status_code == 200
    assert b'upload' in search_response.data

    logout(client)

# Test /storage page access for non-logged-in users
def test_admin_storage_access_non_logged_in_user(client):
    response = client.get('/admin_storage', follow_redirects=True)
    assert response.status_code == 200
    assert b'Login' in response.data

# Test /storage page access for logged-in users
def test_admin_storage_access_logged_in_user(client):
    login(client, valid_username, valid_password)

    storage_response = client.get('/admin_storage', follow_redirects=True)
    assert storage_response.status_code == 200
    assert b'storage' in storage_response.data

    logout(client)
