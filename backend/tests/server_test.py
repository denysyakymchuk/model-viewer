import requests

url = 'http://localhost:90/api'
test_object = 'free__bread_pack_cs2.glb'
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyNzMxM2EyYy1mNzkxLTRhMjMtOWRiZi0wOGM2OTRkODVhZTgiLCJhdWQiOlsiZmFzdGFwaS11c2VyczphdXRoIl0sImV4cCI6MTcwNjUyNjY2Mn0.kgxNNHlwO2B2BQuhdIFjbaSNNELnmskcvl2cZWBdLhw"
headers = {'Authorization': f'Bearer {access_token}'}


class TestServerClass:
    def test_get(self):
        assert requests.get(f'{url}/models').status_code == 200


    def test_get_one(self):
        assert requests.get(f'{url}/models?path_id=2').status_code == 200


    def test_post(self):
        with open('free_1975_porsche_911_930_turbo.glb', 'rb') as f:
            files = {'file': ('free_1975_porsche_911_930_turbo.glb', f)}
            response = requests.post(f'{url}/upload-model', headers=headers, files=files)
            assert response.status_code == 200

    def test_auth_route(self):
        response = requests.get(f'{url}/authenticated-route', headers=headers)
        assert response.status_code == 200

