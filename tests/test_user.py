import pytest
from app import create_app
from .utils import login, logout, valid_username, valid_password

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


## Test module/user ##

# Test /account page access for non-logged-in users
def test_user_account_access_non_logged_in_user(client):
    response = client.get('/account', follow_redirects=True)
    assert response.status_code == 200
    assert b'Login' in response.data

# Test /account page access for logged-in users
def test_user_account_access_logged_in_user(client):
    # Use login utility
    login(client, valid_username, valid_password)

    # Access the /account page
    account_response = client.get('/account', follow_redirects=True)
    assert account_response.status_code == 200
    assert b'Account' in account_response.data

    # Log out
    logout(client)

# Test /search page access for non-logged-in users
def test_user_search_access_non_logged_in_user(client):
    response = client.get('/search', follow_redirects=True)
    assert response.status_code == 200
    assert b'Login' in response.data

# Test /search page access for logged-in users
def test_user_search_access_logged_in_user(client):
    login(client, valid_username, valid_password)

    search_response = client.get('/search', follow_redirects=True)
    assert search_response.status_code == 200
    assert b'Search' in search_response.data

    logout(client)

# Test /site page access for non-logged-in users
def test_user_site_access_non_logged_in_user(client):
    response = client.get('/', follow_redirects=True)
    assert response.status_code == 200
    assert b'Login' in response.data

# Test /site page access for logged-in users
def test_user_site_access_logged_in_user(client):
    login(client, valid_username, valid_password)

    site_response = client.get('/', follow_redirects=True)
    assert site_response.status_code == 200
    assert b'Home' in site_response.data

    logout(client)

# Test /storage page access for non-logged-in users
def test_user_storage_access_non_logged_in_user(client):
    response = client.get('/storage', follow_redirects=True)
    assert response.status_code == 200
    assert b'Login' in response.data

# Test /storage page access for logged-in users
def test_user_storage_access_logged_in_user(client):
    login(client, valid_username, valid_password)

    storage_response = client.get('/storage', follow_redirects=True)
    assert storage_response.status_code == 200
    assert b'Storage' in storage_response.data

    logout(client)
