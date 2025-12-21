import requests
from CompanyApi import CompanyApi

api = CompanyApi("http://5.101.50.27:8000")

# получить компании
def test_get_companies():
    body = api.get_company_list()
    assert len(body) > 0  # == x
    #assert resp.status_code == 200

# Проверка получения активных компаний
def test_get_active_companies():
    full_list = api.get_company_list()
    filtered_list = api.get_company_list(params_to_add={'active' : 'true'})
    assert len(full_list) > len(filtered_list)

# добавить новую компанию
def test_add_new():
    body = api.get_company_list()
    len_before = len(body)
    name = 'Новая'
    descr =  'Урок'
    api.create_company(name, descr)

    body = api.get_company_list()
    len_after = len(body)

    assert len_after - len_before == 1
    assert body[-1]["name"] == name
    assert body[-1]["description"] == descr

# получить компанию по ID
def test_get_one_company():
    # Создаем компанию
    name = "VS Code"
    descr = "IDE"
    result = api.create_company(name, descr)
    new_id = result["id"]

    # Обращаемся к компании
    new_company = api.get_company(new_id)

    # Проверим название, описание и статус новой компании:
    assert new_company["id"] ==  new_id
    assert new_company["name"] == name
    assert new_company["description"] == descr
    assert new_company["is_active"] is True

# изменить информацию о компании
def test_edit():
    name = "Company to be edited"
    descr = "Edit me"
    result = api.create_company(name, descr)
    new_id = result["id"]

    new_name = "Updated"
    new_descr = "_upd_"

    edited = api.edit_company(new_id, new_name, new_descr)

    # Проверяем, что название компании поменялось
    assert edited["name"] == new_name
    # Проверяем, что описание компании поменялось
    assert edited["description"] == new_descr

# удалить компанию
def test_delete():
    name = "Company to be deleted"
    descr = "Delete me"
    result = api.create_company(name, descr)
    new_id = result["id"]

    # Обращаемся к компании
    new_company = api.get_company(new_id)
    # Проверим название, описание и статус компании:
    assert new_company["name"] == name
    assert new_company["description"] == descr
    assert new_company["is_active"] is True

    # Получаем список компаний и сохраняем его длину
    body = api.get_company_list()
    len_before = len(body)

    # Удаляем компанию
    api.delete_company(new_id)

    # Проверяем, что список компаний меньше на 1
    body = api.get_company_list()
    len_after = len(body)
    assert len_before- len_after == 1

    # Проверяем, что удаленная компания не находится по id
    deleted = api.get_company(new_id)
    assert deleted['detail'] == 'Компания не найдена'

# деактивировать компанию
def test_deactivate():
    # Создаем компанию
    name = "Company to be deactivated"
    result = api.create_company(name)
    new_id = result["id"]
    # Деактивируем компанию
    body = api.set_active_state(new_id, False)

    # Проверяем, что у компании статус «неактивная»
    assert body["is_active"] is False

# деактивировать и снова активировать компанию.
def test_deactivate_and_activate_back():
    #Создаем компанию:
    name = "Company to be deactivated"
    result = api.create_company(name)
    new_id = result["id"]

    # Деактивируем компанию с помощью параметра False
    body_d = api.set_active_state(new_id, False)
    # Проверяем, что компания не активная
    assert body_d["is_active"] is False

    # Активируем компанию с помощью параметра True
    body_a = api.set_active_state(new_id, True)
    # Проверяем, что компания активная
    assert body_a["is_active"] is True