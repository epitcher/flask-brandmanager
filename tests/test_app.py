import pytest
from app import create_app

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

# ... (tests) ...

def test_favicon(client):
    response = client.get('/favicon.ico')
    assert response.status_code == 200
    assert response.mimetype == 'image/vnd.microsoft.icon'

def test_login_get(client):
    response = client.get('/login')
    print(response.data)
    assert response.status_code == 200
    assert b'Login' in response.data

def test_login_post_valid_credentials(client):
    response = client.post('/login', data=dict(username=valid_username, password=valid_password), follow_redirects=True)
    assert response.status_code == 200
    assert b'Browse Materials' in response.data

def test_login_post_invalid_credentials(client):
    response = client.post('/login', data=dict(username=invalid_username, password=invalid_password), follow_redirects=True)
    assert response.status_code == 401

def login(client, username, password):
    return client.post('/login', data=dict(username=username, password=password), follow_redirects=True)

def logout(client):
    return client.get('/logout', follow_redirects=True)

def test_logout(client):
    # Log in with valid credentials (replace 'valid_username' and 'valid_password' with actual valid credentials)
    login_response = login(client, valid_username, valid_password)
    assert b'Browse Materials' in login_response.data

    # Log out
    logout_response = logout(client)
    assert logout_response.status_code == 200
    assert b'Logged out successfully' in logout_response.data
    assert b'Login' in logout_response.data