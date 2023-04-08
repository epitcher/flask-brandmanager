valid_username = "user"
valid_password = "user"
invalid_username = "invalid"
invalid_password = "invalid"

def login(client, username, password):
    return client.post('/login', data=dict(username=username, password=password), follow_redirects=True)

def logout(client):
    return client.get('/logout', follow_redirects=True)