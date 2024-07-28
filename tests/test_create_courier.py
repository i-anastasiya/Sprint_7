import allure
import requests

from total_information import TotalInformation
from datails import Text


class TestCreateCourier:

    @allure.description('Проверяем, что нельзя создать два одинаковых курьера')
    def test_cannot_create_two_couriers(self):
        method = TotalInformation()
        rqst = method.register_new_courier_and_return_login_password()
        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=rqst)
        two_couriers = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=rqst)

        assert two_couriers.status_code == 409 and two_couriers.json()['message'] == Text.LOGIN_ALREADY_USAGE

    @allure.description('Проверяем создание курьера, когда передаем в ручку все обязательные поля')
    def test_create_user(self, create_courier_user):
        rqst = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=create_courier_user)
        assert rqst.status_code == 201 and rqst.text == Text.USER_CREATION_SUCCESS

    @allure.description('Проверяем, что если одного из полей нет, запрос возвращает ошибку')
    def test_no_password(self):
        method = TotalInformation()
        rqst = method.register_new_courier_and_return_login_password()
        rqst['password'] = ''
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=rqst)

        assert response.status_code == 400 and response.json()['message'] == Text.INSUFFICIENT_DATA_CREATE_USER

    @allure.description('Проверяем, что если создать пользователя с логином, который уже есть, возвращается ошибка.')
    def test_existing_login(self):
        method = TotalInformation()
        rqst = method.register_new_courier_and_return_login_password()
        existing_login = 'existing_user'
        rqst['login'] = existing_login
        fail_user = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=rqst)

        assert fail_user.status_code == 409 and fail_user.json()['message'] == Text.LOGIN_ALREADY_USAGE
