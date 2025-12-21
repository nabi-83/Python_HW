import requests

base_url = "https://ru.yougile.com/api-v2"

def test_simple_req():
    resp = requests.get(base_url+'/auth/companies')

    response_body = resp.json()
    first_company = response_body[0]

    assert first_company["name"] == "QA Студия 'ТестировщикЪ'"
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"
    resp.json()

def test_auth():
    creds = {
        'username': 'harrypotter',
        'password': 'expelliarmus'
    }
    resp = requests.post(base_url + '/auth/login', json=creds)
    assert resp.json()["user_token"] is not None
    assert resp.status_code == 200

def test_create_company():
    creds = {
        'username': 'harrypotter',
        'password': 'expelliarmus'
    }

    company = {
        "name": "python",
        "description": "requests"
    }

    #авторизация
    resp = requests.post(base_url+'/auth/login', json=creds)
    token = resp.json()["userToken"]

    #создание
    my_headers= {}
    my_headers["x-client-token"] = token

    resp = requests.post(base_url+'/company/create', json=company, headers=my_headers)
    assert resp.status_code == 201

