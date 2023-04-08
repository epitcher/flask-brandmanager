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


# Test favicon
def test_favicon(client):
    response = client.get('/favicon.ico')
    assert response.status_code == 200
    assert response.mimetype == 'image/vnd.microsoft.icon'

# Test login page
def test_login_get(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Login' in response.data

# Test valid login credentials
def test_login_post_valid_credentials(client):
    response = login(client, valid_username, valid_password)
    assert response.status_code == 200
    assert b'Browse Materials' in response.data

# Test invalid login credentials
def test_login_post_invalid_credentials(client):
    response = login(client, invalid_username, invalid_password)
    assert response.status_code == 401

# Test logout functionality
def test_logout(client):
    # Log in with valid credentials
    login_response = login(client, valid_username, valid_password)
    assert b'Browse Materials' in login_response.data

    # Log out
    logout_response = logout(client)
    assert logout_response.status_code == 200
    assert b'Logged out successfully' in logout_response.data
    assert b'Login' in logout_response.data

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



## Test Errors ##

# Test 404 error page
def test_404_page(client):
    response = client.get('/nonexistent_route')
    assert response.status_code == 404
    assert b'404' in response.data # Expand?
