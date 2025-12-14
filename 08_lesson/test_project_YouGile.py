from project_YouGile import ProjectYouGile
from test_data import (LOGIN, PASSWORD, COMPANY_ID, NEW_TITLE,
                       TEST_USER, TITLE_GET_TEST, TITLE_EDIT_TEST,
                       EDITED_TITLE, DELETED_STATUS, NEW_TITLE_NEGATIVE,
                       TEST_USER_NEGATIVE)


# Экземпляр API
api = ProjectYouGile('https://ru.yougile.com/api-v2/',
                     LOGIN, PASSWORD, COMPANY_ID)


def test_create_project_positive():
    # Количество проектов до
    projects_before = api.get_project_list()
    len_before = len(projects_before)

    # Создание проекта
    result = api.create_project(NEW_TITLE, TEST_USER)
    new_id = result.json()['id']

    # Количество проектов после
    projects_after = api.get_project_list()
    len_after = len(projects_after)

    assert result.status_code == 201
    assert len_after - len_before == 1
    assert projects_after[-1]['title'] == NEW_TITLE
    assert projects_after[-1]['id'] == new_id

    # Очистка данных после теста
    api.edit_project(new_id, True,
                     NEW_TITLE, TEST_USER)


def test_create_project_negative():
    projects_before = api.get_project_list()
    len_before = len(projects_before)

    # Создание проекта с пустым названием
    result = api.create_project(NEW_TITLE_NEGATIVE, TEST_USER)

    # Количество проектов после
    projects_after = api.get_project_list()
    len_after = len(projects_after)

    assert result.status_code == 400
    assert len_after - len_before == 0


def test_get_project_with_id_positive():
    result = api.create_project(TITLE_GET_TEST, TEST_USER)
    project_id = result.json()['id']

    # Обращаемся к проекту
    new_project = api.get_project_with_id(project_id)

    assert new_project.status_code == 200
    assert new_project.json()['title'] == TITLE_GET_TEST
    assert new_project.json()['users'] == TEST_USER

    # Очистка данных после теста
    api.edit_project(project_id, True,
                     TITLE_GET_TEST, TEST_USER)


def test_get_project_with_id_negative():
    # Обращаемся к проекту с несуществующим  id
    new_project = api.get_project_with_id("9999")

    assert new_project.status_code == 404


def test_edit_project_positive():
    # Создание проекта
    result = api.create_project(TITLE_EDIT_TEST, TEST_USER)
    project_id = result.json()['id']

    # Изменение проекта
    edited = api.edit_project(project_id, DELETED_STATUS,
                              EDITED_TITLE, TEST_USER)

    assert edited.status_code == 200
    project_title = api.get_project_with_id(project_id).json()['title']
    assert project_title == EDITED_TITLE

    # Очистка данных после теста
    api.edit_project(project_id, True,
                     EDITED_TITLE, TEST_USER)


def test_edit_project_negative():
    # Создание проекта
    result = api.create_project(TITLE_EDIT_TEST, TEST_USER)
    project_id = result.json()['id']

    # Попытка змененить проект с неверным идентификатором роли
    edited = api.edit_project(project_id, DELETED_STATUS,
                              EDITED_TITLE, TEST_USER_NEGATIVE)

    assert edited.status_code == 400

    # Очистка данных после теста
    api.edit_project(project_id, True,
                     EDITED_TITLE, TEST_USER)