import requests

from dotenv import dotenv_values

# load env variables. They are collection
variables = dotenv_values(".env")

url = variables["URL"]
username = variables["USERNAME"]
password = variables["PASSWORD"]

def login():
    access_token = requests.post(f'{url}/auth/jwt/login', {'username': username, 'password': password},
                                 headers={'Content-Type': 'application/x-www-form-urlencoded'}).json()["access_token"]
    headers = {'Authorization': f'Bearer {access_token}'}
    return headers


class TestServerClass:
    def test_login(self):
        access_token = requests.post(f'{url}/auth/jwt/login', {'username': username, 'password':password}, headers={'Content-Type':'application/x-www-form-urlencoded'})
        assert access_token.status_code == 200

    def test_get_all(self):
        assert requests.get(f'{url}/models').status_code == 200

    def test_get_one(self):
        assert requests.get(f'{url}/models?path_id=2').status_code == 200

    def test_post(self):
        headers = login()
        with open('test_storage/free_1975_porsche_911_930_turbo.glb', 'rb') as f:
            files = {'file': ('free_1975_porsche_911_930_turbo.glb', f)}
            response = requests.post(f'{url}/upload-model', headers=headers, files=files)
            assert response.status_code == 200

    def test_post_fail(self):
        headers = login()
        with open('test_storage/test_file', 'rb') as f:
            files = {'file': ('test_file', f)}
            response = requests.post(f'{url}/upload-model', headers=headers, files=files)
            assert response.status_code == 422

    def test_delete(self):
        headers = login()
        assert requests.get(f'{url}/delete-model?path_id=2', headers=headers).status_code == 200


    def test_auth_route(self):
        headers = login()
        response = requests.get(f'{url}/authenticated-route', headers=headers)
        assert response.status_code == 200

