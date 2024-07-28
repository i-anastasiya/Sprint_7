import allure
import requests


from total_information import TotalInformation
from datails import Text

class TestLogin:
    @allure.description('Проверяем, что  курьер может авторизоваться')
    def test_login_courier_user(self, create_courier_user):
        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=create_courier_user)
        del create_courier_user['firstName']
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=create_courier_user)
        assert response.status_code == 200 and 'id' in response.text

    @allure.description('Проверяем что если какого-то поля нет, запрос возвращает ошибку')
    def test_no_login_courier_user(self):
        method = TotalInformation()
        rqst = method.register_new_courier_and_return_login_password()
        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=rqst)
        del rqst['firstName']
        rqst['login'] = ''
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=rqst)

        assert response.status_code == 400 and response.json()['message'] == Text.INSUFFICIENT_DATA_FOR_ACCOUNTING

    @allure.description('Проверяем, что система вернёт ошибку, если неправильно указать логин или пароль;')
    def test_wrong_password(self):
        method = TotalInformation()
        rqst = method.register_new_courier_and_return_login_password()
        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=rqst)
        del rqst['firstName']
        rqst['password'] = '57842-93'
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=rqst)

        assert response.status_code == 404 and response.json()['message'] == Text.ACCOUNT_NOT_FOUND

    @allure.description('Проверяем, что если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    def test_no_user(self):
        method = TotalInformation()
        rqst = method.register_new_courier_and_return_login_password()
        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=rqst)
        del rqst['firstName']
        rqst['password'] = '289304830'
        rqst['login'] = '№;(№)'
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=rqst)

        assert response.status_code == 404 and response.json()['message'] == Text.ACCOUNT_NOT_FOUND
