import requests
import json


def test_loggedin_user_info():
    url = "https://api.clockify.me/api/v1/user"

    payload = {}
    headers = {
        'x-api-key': 'YzNlNjRlM2UtYWE3Yy00Nzk1LTg4YWYtMTUzMjUzMDY5ZTNj'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.status_code==200
    print(response.text)


def test_workspaces():
    url = "https://api.clockify.me/api/v1/workspaces"

    payload = {}
    headers = {
        'x-api-key': 'YzNlNjRlM2UtYWE3Yy00Nzk1LTg4YWYtMTUzMjUzMDY5ZTNj'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.status_code == 200
    print(response.text)


def test_add_workspace():
    url = "https://api.clockify.me/api/v1/workspaces"

    payload = json.dumps({
        "name": "New_Sample_Workspace1"
    })
    headers = {
        'x-api-key': 'YzNlNjRlM2UtYWE3Yy00Nzk1LTg4YWYtMTUzMjUzMDY5ZTNj',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    assert response.status_code == 200
    print(response.text)


def test_find_clients():
    url = "https://api.clockify.me/api/v1/workspaces/6553c1c4e7f1e3635babb778/clients/"

    payload = {}
    headers = {
        'x-api-key': 'YzNlNjRlM2UtYWE3Yy00Nzk1LTg4YWYtMTUzMjUzMDY5ZTNj'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.status_code == 200
    print(response.text)


def test_get_webhooks():
    url = "https://api.clockify.me/api/v1/workspaces/6553c1c4e7f1e3635babb778/webhooks"

    payload = {}
    headers = {
        'x-api-key': 'YzNlNjRlM2UtYWE3Yy00Nzk1LTg4YWYtMTUzMjUzMDY5ZTNj'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.status_code == 200
    print(response.text)


def test_get_projects():
    url = "https://api.clockify.me/api/v1/workspaces/6553c1c4e7f1e3635babb778/projects"

    payload = {}
    headers = {
        'x-api-key': 'YzNlNjRlM2UtYWE3Yy00Nzk1LTg4YWYtMTUzMjUzMDY5ZTNj'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.status_code == 200
    print(response.text)


def test_add_new_client():
    url = "https://api.clockify.me/api/v1/workspaces/6553c1c4e7f1e3635babb778/clients"

    payload = json.dumps({
        "address": "42 King street",
        "email": "Dollerama@gmail.com",
        "name": "Dollerama",
        "note": "Sample Note"
    })
    headers = {
        'x-api-key': 'YzNlNjRlM2UtYWE3Yy00Nzk1LTg4YWYtMTUzMjUzMDY5ZTNj',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    assert response.status_code == 200
    print(response.text)


def test_get_client_byID():
    url = "https://api.clockify.me/api/v1/workspaces/6553c1c4e7f1e3635babb778/clients/656767d6dfd0e6033efc2e85"

    payload = {}
    headers = {
        'x-api-key': 'YzNlNjRlM2UtYWE3Yy00Nzk1LTg4YWYtMTUzMjUzMDY5ZTNj'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.status_code == 200
    print(response.text)


def test_update_client():
    url = "https://api.clockify.me/api/v1/workspaces/6553c1c4e7f1e3635babb778/clients/656767d6dfd0e6033efc2e85"

    payload = json.dumps({
        "address": "46 King street",
        "archived": True,
        "email": "dollerama@gmail.com",
        "name": "Dollerama",
        "note": "Sample_Note1"
    })
    headers = {
        'x-api-key': 'YzNlNjRlM2UtYWE3Yy00Nzk1LTg4YWYtMTUzMjUzMDY5ZTNj',
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)
    assert response.status_code == 201
    print(response.text)


def test_find_tags():
    url = "https://api.clockify.me/api/v1/workspaces/6553c1c4e7f1e3635babb778/tags"

    payload = {}
    headers = {
        'x-api-key': 'YzNlNjRlM2UtYWE3Yy00Nzk1LTg4YWYtMTUzMjUzMDY5ZTNj'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.status_code == 200
    print(response.text)


def test_add_new_tag():
    url = "https://api.clockify.me/api/v1/workspaces/6553c1c4e7f1e3635babb778/tags"

    payload = json.dumps({
        "name": "Tags101"
    })
    headers = {
        'x-api-key': 'YzNlNjRlM2UtYWE3Yy00Nzk1LTg4YWYtMTUzMjUzMDY5ZTNj',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    assert response.status_code == 200
    print(response.text)


def test_get_tags_byID():
    url = "https://api.clockify.me/api/v1/workspaces/6553c1c4e7f1e3635babb778/tags/65676bbf478749252d1c3f06"

    payload = {}
    headers = {
        'x-api-key': 'YzNlNjRlM2UtYWE3Yy00Nzk1LTg4YWYtMTUzMjUzMDY5ZTNj'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.status_code == 200
    print(response.text)


def test_find_groups():
    url = "https://api.clockify.me/api/v1/workspaces/6553c1c4e7f1e3635babb778/user-groups"

    payload = {}
    headers = {
        'x-api-key': 'YzNlNjRlM2UtYWE3Yy00Nzk1LTg4YWYtMTUzMjUzMDY5ZTNj'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.status_code == 200
    print(response.text)


def test_add_new_group():
    url = "https://api.clockify.me/api/v1/workspaces/6553c1c4e7f1e3635babb778/user-groups"

    payload = json.dumps({
        "name": "Sample_Group2"
    })
    headers = {
        'x-api-key': 'YzNlNjRlM2UtYWE3Yy00Nzk1LTg4YWYtMTUzMjUzMDY5ZTNj',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    assert response.status_code == 200
    print(response.text)


def test_add_user_to_group():
    url = "https://api.clockify.me/api/v1/workspaces/6553c1c4e7f1e3635babb778/user-groups/65676d4d478749252d1c41fc/users"

    payload = json.dumps({
        "userId": "6553c1c4e7f1e3635babb777"
    })
    headers = {
        'x-api-key': 'YzNlNjRlM2UtYWE3Yy00Nzk1LTg4YWYtMTUzMjUzMDY5ZTNj',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    assert response.status_code == 200
    print(response.text)


def test_find_task():
    url = "https://api.clockify.me/api/v1/workspaces/6553c1c4e7f1e3635babb778/projects/6553c3d5e7f1e3635babf7d8/tasks"

    payload = {}
    headers = {
        'x-api-key': 'YzNlNjRlM2UtYWE3Yy00Nzk1LTg4YWYtMTUzMjUzMDY5ZTNj'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.status_code == 200
    print(response.text)


def test_get_custom_field():
    url = "https://api.clockify.me/api/v1/workspaces/6553c1c4e7f1e3635babb778/custom-fields"

    payload = {}
    headers = {
        'x-api-key': 'YzNlNjRlM2UtYWE3Yy00Nzk1LTg4YWYtMTUzMjUzMDY5ZTNj'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.status_code == 200
    print(response.text)


def test_get_all_expenses():
    url = "https://api.clockify.me/api/v1/workspaces/6553c1c4e7f1e3635babb778/expenses"

    payload = {}
    headers = {
        'x-api-key': 'YzNlNjRlM2UtYWE3Yy00Nzk1LTg4YWYtMTUzMjUzMDY5ZTNj'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.status_code == 200
    print(response.text)


def test_add_expense_category():
    url = "https://api.clockify.me/api/v1/workspaces/6553c1c4e7f1e3635babb778/expenses/categories"

    payload = json.dumps({
        "hasUnitPrice": True,
        "name": "Sample_expense03",
        "priceInCents": 1100,
        "unit": "USD"
    })
    headers = {
        'x-api-key': 'YzNlNjRlM2UtYWE3Yy00Nzk1LTg4YWYtMTUzMjUzMDY5ZTNj',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    assert response.status_code == 200
    print(response.text)


def test_del_client():
    url = "https://api.clockify.me/api/v1/workspaces/6553c1c4e7f1e3635babb778/clients/656767d6dfd0e6033efc2e85"

    payload = {}
    headers = {
        'x-api-key': 'YzNlNjRlM2UtYWE3Yy00Nzk1LTg4YWYtMTUzMjUzMDY5ZTNj'
    }

    response = requests.request("DELETE", url, headers=headers, data=payload)
    assert response.status_code == 200
    print(response.text)
