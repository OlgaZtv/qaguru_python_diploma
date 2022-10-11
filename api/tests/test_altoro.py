from pytest_voluptuous import S

from api.data.data import SUCCESSFUL, login
from api.utils.sessions import altoro


def test_login():
    payload = {"username": 'admin', 'password': "admin"}
    headers = {'content-type': 'application/json'}
    response = altoro().post('/login', headers=headers, json=payload)
    assert response.status_code == SUCCESSFUL, f'Status code should be {SUCCESSFUL}'
    assert S(login) == response.json()


def test_transfer():
    payload = {"username": 'admin', 'password': "admin"}
    headers_login = {'content-type': 'application/json'}
    response_login = altoro().post('/login', headers=headers_login, json=payload)
    text = response_login.text
    token: str = str(text[18:49])
    headers = {'content-type': 'application/json', 'Authorization': token}
    data = {"toAccount": "800002", "fromAccount": "800003", "transferAmount": "200"}
    response = altoro().post('/transfer', headers=headers, json=data)
    assert response.status_code == SUCCESSFUL, f'Status code should be {SUCCESSFUL}'


def test_submit_and_review_feedback():
    body = {"name": "J Smith", "email": "jsmtih@altoromutual.com", "subject": "Amazing web design",
            "message": "I like the new look of your applicaiton"}
    headers = {'content-type': 'application/json'}
    response = altoro().post('/feedback/submit', headers=headers, json=body)
    assert response.status_code == SUCCESSFUL, f'Status code should be {SUCCESSFUL}'


def test_add_user():
    payload = {"username": 'admin', 'password': "admin"}
    headers_login = {'content-type': 'application/json'}
    response_login = altoro().post('/login', headers=headers_login, json=payload)
    text = response_login.text
    token: str = str(text[18:49])
    headers = {'content-type': 'application/json', 'Authorization': token}
    data = {"firstname": "Bilbo",
            "lastname": "Baggins",
            "username": "bilbob",
            "password1": "S3l3ctS0methingStr0ng5AsP@ssword",
            "password2": "S3l3ctS0methingStr0ng5AsP@ssword"}
    response = altoro().post('/admin/addUser', headers=headers, json=data)
    assert response.status_code == SUCCESSFUL, f'Status code should be {SUCCESSFUL}'


def test_change_user_password():
    payload = {"username": 'admin', 'password': "admin"}
    headers_login = {'content-type': 'application/json'}
    response_login = altoro().post('/login', headers=headers_login, json=payload)
    text = response_login.text
    token: str = str(text[18:49])
    headers = {'content-type': 'application/json', 'Authorization': token}
    data = {
        "username": "jdoe",
        "password1": "Th1s!sz3nu3Passv0rd",
        "password2": "Th1s!sz3nu3Passv0rd"
    }
    response = altoro().post('/admin/changePassword', headers=headers, json=data)
    assert response.status_code == SUCCESSFUL, f'Status code should be {SUCCESSFUL}'


def test_logout():
    response = altoro().get('/logout')
    assert response.status_code == SUCCESSFUL, f'Status code should be {SUCCESSFUL}'
