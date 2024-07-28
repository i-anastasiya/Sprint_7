import allure
import pytest
import requests
from datails import DatailsUsers


class TestCreateOrder:
    user_details = DatailsUsers.datails_user
    @pytest.mark.parametrize("firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, "
                             "color", user_details)

    @allure.description('Проверяем создание заказа со всеми параметрами')
    def test_create_order_with_color(self, firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color):
        data = {
            "firstName": firstName,
            "lastName": lastName,
            "address": address,
            "metroStation": metroStation,
            "phone": phone,
            "rentTime": rentTime,
            "deliveryDate": deliveryDate,
            "comment": comment,
            "color": [color],
        }
        rqst = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', json=data)
        assert rqst.status_code == 201
        assert 'track' in rqst.text
