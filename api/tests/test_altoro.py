import allure
from pytest_voluptuous import S

from api.schemas.schemas import SUCCESSFUL, login
from api.utils.sessions import altoro


@allure.tag("api")
@allure.label('owner', 'zatulivetrova')
@allure.feature('API')
@allure.story('Authorization')
def test_login():
    # GIVEN
    payload = {"username": 'admin', 'password': "admin"}
    headers = {'content-type': 'application/json'}

    # WHEN
    response = altoro().post('/login', headers=headers, json=payload)

    # THEN
    assert response.status_code == SUCCESSFUL, f'Status code should be {SUCCESSFUL}'
    assert S(login) == response.json()


@allure.tag("api")
@allure.label('owner', 'zatulivetrova')
@allure.feature('API')
@allure.story('Transfer test')
def test_transfer():
    # GIVEN
    payload = {"username": 'admin', 'password': "admin"}
    headers_login = {'content-type': 'application/json'}

    # WHEN
    response_login = altoro().post('/login', headers=headers_login, json=payload)
    text = response_login.text
    token: str = str(text[18:49])
    headers = {'content-type': 'application/json', 'Authorization': token}
    data = {"toAccount": "800002", "fromAccount": "800003", "transferAmount": "200"}
    response = altoro().post('/transfer', headers=headers, json=data)

    # THEN
    assert response.status_code == SUCCESSFUL, f'Status code should be {SUCCESSFUL}'


@allure.tag("api")
@allure.label('owner', 'zatulivetrova')
@allure.feature('API')
@allure.story('Feedback')
def test_submit_and_review_feedback():
    # GIVEN
    body = {"name": "J Smith", "email": "jsmtih@altoromutual.com", "subject": "Amazing web design",
            "message": "I like the new look of your applicaiton"}

    # WHEN
    response = altoro().post('/feedback/submit', json=body)

    # THEN
    assert response.status_code == SUCCESSFUL, f'Status code should be {SUCCESSFUL}'


@allure.tag("api")
@allure.label('owner', 'zatulivetrova')
@allure.feature('API')
@allure.story('Add user')
def test_add_user():
    # GIVEN
    payload = {"username": 'admin', 'password': "admin"}

    # WHEN
    response_login = altoro().post('/login', json=payload)
    text = response_login.text
    token: str = str(text[18:49])
    headers = {'content-type': 'application/json', 'Authorization': token}
    data = {"firstname": "Bilbo",
            "lastname": "Baggins",
            "username": "bilbob",
            "password1": "S3l3ctS0methingStr0ng5AsP@ssword",
            "password2": "S3l3ctS0methingStr0ng5AsP@ssword"}
    response = altoro().post('/admin/addUser', headers=headers, json=data)

    # THEN
    assert response.status_code == SUCCESSFUL, f'Status code should be {SUCCESSFUL}'


@allure.tag("api")
@allure.label('owner', 'zatulivetrova')
@allure.feature('API')
@allure.story('Change password')
def test_change_user_password():
    # GIVEN
    payload = {"username": 'admin', 'password': "admin"}

    # WHEN
    response_login = altoro().post('/login', json=payload)
    text = response_login.text
    token: str = str(text[18:49])
    headers = {'content-type': 'application/json', 'Authorization': token}
    data = {
        "username": "jdoe",
        "password1": "Th1s!sz3nu3Passv0rd",
        "password2": "Th1s!sz3nu3Passv0rd"
    }
    response = altoro().post('/admin/changePassword', headers=headers, json=data)

    # THEN
    assert response.status_code == SUCCESSFUL, f'Status code should be {SUCCESSFUL}'


@allure.tag("api")
@allure.label('owner', 'zatulivetrova')
@allure.feature('API')
@allure.story('Log out test')
def test_logout():
    # WHEN
    response = altoro().get('/logout')

    # THEN
    assert response.status_code == SUCCESSFUL, f'Status code should be {SUCCESSFUL}'
