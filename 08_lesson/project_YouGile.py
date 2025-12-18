import requests


class ProjectYouGile:
    # Инициализация
    def __init__(self, url, login, password, company) -> None:
        self.url = url
        self.token = self.get_token(login, password, company)

    # Получить ключ авторизации
    def get_token(self, login, password, company):
        payload = {
            "login": login,
            "password": password,
            "companyId": company
        }
        resp = requests.post(self.url + 'auth/keys/get', json=payload)

        response_data = resp.json()
        return response_data[0]['key']

    # Получить список проектов компании
    def get_project_list(self):
        key = self.token
        headers = {
            'Authorization': f'Bearer {key}'
        }
        resp = requests.get(self.url + 'projects', headers=headers)
        return resp.json()["content"]

    # Добавить компанию:
    def create_project(self, title, users):
        key = self.token
        headers = {
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'application/json; charset=utf-8'
        }
        project = {
            "title": title,
            "users": users
        }
        resp = requests.post(self.url + 'projects',
                             headers=headers,
                             json=project)
        return resp

    # Получить проект по id
    def get_project_with_id(self, project_id):
        key = self.token
        headers = {
            'Authorization': f'Bearer {key}'
        }
        resp = requests.get(self.url + f'projects/{project_id}',
                            headers=headers)
        return resp

    # Изменить название проекта
    def edit_project(self, project_id, new_deleted, new_title,
                     new_users):
        key = self.token
        headers = {
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'application/json; charset=utf-8'
        }
        project = {
            "deleted": new_deleted,
            "title": new_title,
            "users": new_users
        }
        resp = requests.put(self.url + f'projects/{project_id}',
                            headers=headers, json=project)
        return resp