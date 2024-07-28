import allure
import requests

class TestListOrders:

    @allure.description('Проверяем, что в тело ответа возвращается список заказов.')
    def test_list_orders(self):
        rqst = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders')
        assert rqst.status_code == 200 and 'orders' in rqst.text
