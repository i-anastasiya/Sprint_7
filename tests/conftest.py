import pytest
import requests

from total_information import TotalInformation
from datails import Url


# фикстура создает и удаляет курьера в тестах
@pytest.fixture(scope='function')
def create_courier_user():
    method = TotalInformation()
    data = method.register_new_courier_and_return_login_password()
    yield data
    response = requests.post(Url.LOGIN, data={"login": data['login'], "password": data['password']})
    user_id = response.json()['id']
    requests.delete(f'{Url.DELETE_COURIER}/{user_id}')
