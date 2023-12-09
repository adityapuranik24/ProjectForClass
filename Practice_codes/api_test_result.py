# Name: "Vyomesh Mistry"
# Student Number: "8870525"

import json
import requests


def test_all_User():
    url = "https://api.clockify.me/api/v1/workspaces/654c010bc7d5882517f7e416/users"

    payload = {}
    headers = {
        'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200

    print(response.text)


def test_login_user_info():
    url = "https://api.clockify.me/api/v1/user"

    payload = {}
    headers = {
        'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200

    print(response.text)


def test_all_workspace_expense():
    url = "https://api.clockify.me/api/v1/workspaces/654c010bc7d5882517f7e416/expenses"

    payload = {}
    headers = {
        'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200

    print(response.text)


def test_approval_request():
    url = "https://api.clockify.me/api/v1/workspaces/654c010bc7d5882517f7e416/approval-requests"

    payload = {}
    headers = {
        'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200

    print(response.text)


def test_update_webhooks():
    url = "https://api.clockify.me/api/v1/workspaces/654c010bc7d5882517f7e416/webhooks/65665bb4478749252d1abea7"

    payload = json.dumps({
        "name": "Webhooks10",
        "triggerSource": [],
        "triggerSourceType": "PROJECT_ID",
        "url": "https://docs.clockify.me/#tag/Approval/operation/create_10",
        "webhookEvent": "NEW_TIMER_STARTED"
    })
    headers = {
        'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2',
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    assert response.status_code == 200

    print(response.text)


def test_add_workspaces():
    url = "https://api.clockify.me/api/v1/workspaces"

    payload = json.dumps({
        "name": "workspace6"
    })
    headers = {
        'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.status_code == 400

    print(response.text)


def test_update_client():
    url = "https://api.clockify.me/api/v1/workspaces/654c010bc7d5882517f7e416/clients/65665cbff8bf2b116110a33e"

    payload = json.dumps({
        "address": "string",
        "archived": True,
        "email": "karanpatel44@gmail.com",
        "name": "KirtanPatel",
        "note": "string"
    })
    headers = {
        'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2',
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    assert response.status_code == 200

    print(response.text)


def test_get_custom_field():
    url = "https://api.clockify.me/api/v1/workspaces/654c010bc7d5882517f7e416/custom-fields"

    payload = {}
    headers = {
        'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200

    print(response.text)


def test_set_custom_field():
    url = "https://api.clockify.me/api/v1/workspaces/654c010bc7d5882517f7e416/custom-fields/65666467348b90225e131e01"

    payload = json.dumps({
        "allowedValues": [],
        "description": "string",
        "name": "Custom6",
        "onlyAdminCanEdit": False,
        "placeholder": "Enter Custom6",
        "required": False,
        "status": "INACTIVE",
        "type": "TXT",
        "workspaceDefaultValue": "Type string custom field example value"
    })
    headers = {
        'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2',
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    assert response.status_code == 200

    print(response.text)


def test_update_expense_category():
    url = "https://api.clockify.me/api/v1/workspaces/654c010bc7d5882517f7e416/expenses/categories/65654f9989c23218a2050571"

    payload = json.dumps({
        "hasUnitPrice": True,
        "name": "new4",
        "priceInCents": 0,
        "unit": "string"
    })
    headers = {
        'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2',
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    assert response.status_code == 200

    print(response.text)


def test_all_project_on_workspace():
    url = "https://api.clockify.me/api/v1/workspaces/654c010bc7d5882517f7e416/projects"

    payload = {}
    headers = {
        'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200

    print(response.text)


def test_find_project_id():
    url = "https://api.clockify.me/api/v1/workspaces/654c010bc7d5882517f7e416/projects/656549aa8bce124769811c0c"

    payload = {}
    headers = {
        'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200

    print(response.text)


def test_add_usergroups():
    url = "https://api.clockify.me/api/v1/workspaces/654c010bc7d5882517f7e416/user-groups"

    payload = json.dumps({
        "name": "phone"
    })
    headers = {
        'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.status_code == 400

    print(response.text)


def test_add_tag():
    url = "https://api.clockify.me/api/v1/workspaces/654c010bc7d5882517f7e416/tags"

    payload = json.dumps({
        "name": "string4"
    })
    headers = {
        'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.status_code == 201

    print(response.text)


def test_add_client_on_workspace():
    url = "https://api.clockify.me/api/v1/workspaces/654c010bc7d5882517f7e416/clients"

    payload = json.dumps({
        "address": "string",
        "email": "vyommistry22@gmail.com",
        "name": "Kirtan",
        "note": "string"
    })
    headers = {
        'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.status_code == 400

    print(response.text)


def test_create_webhooks():
    print("Create Webhooks API Response", end="\n\n")
    url = "https://api.clockify.me/api/v1/workspaces/654c010bc7d5882517f7e416/webhooks"

    payload = json.dumps({
        "name": "Webhooks0",
        "triggerSource": [],
        "triggerSourceType": "PROJECT_ID",
        "url": "https://docs.clockify.me/#tag/Approval/operation/create_10",
        "webhookEvent": "NEW_TIMER_STARTED"
    })
    headers = {
        'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def test_update_webhooks():
    print("Update Webhooks API Response", end="\n\n")
    url = "https://api.clockify.me/api/v1/workspaces/654c010bc7d5882517f7e416/webhooks/65665bb4478749252d1abea7"

    payload = json.dumps({
        "name": "Webhooks10",
        "triggerSource": [],
        "triggerSourceType": "PROJECT_ID",
        "url": "https://docs.clockify.me/#tag/Approval/operation/create_10",
        "webhookEvent": "NEW_TIMER_STARTED"
    })
    headers = {
        'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2',
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)


def test_add_invoice():
    url = "https://api.clockify.me/api/v1/workspaces/654c010bc7d5882517f7e416/invoices"

    payload = json.dumps({
        "clientId": "65654c5b2a47c52a012f6207",
        "currency": "string",
        "dueDate": "2019-08-24T14:15:22Z",
        "issuedDate": "2019-08-24T14:15:22Z",
        "number": "string"
    })
    headers = {
        'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.status_code == 201

    print(response.text)


def test_get_all_expense_category():
    url = "https://api.clockify.me/api/v1/workspaces/654c010bc7d5882517f7e416/expenses/categories"

    payload = {}
    headers = {
        'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200

    print(response.text)


def test_find_tasks():
    url = "https://api.clockify.me/api/v1/workspaces/654c010bc7d5882517f7e416/projects/656549aa8bce124769811c0c/tasks"

    payload = {}
    headers = {
        'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200

    print(response.text)


def test_get_task_by_id():
    url = "https://api.clockify.me/api/v1/workspaces/654c010bc7d5882517f7e416/projects/656549aa8bce124769811c0c/tasks/656760cc34cfa45c73459fc"

    payload = {}
    headers = {
        'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 400

    print(response.text)
