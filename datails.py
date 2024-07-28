class Url:
    CREATE_ORDERS = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
    CREATE_COURIER = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
    RECEIVING_ORDERS = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
    LOGIN = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
    DELETE_COURIER = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
class Text:
    USER_CREATION_SUCCESS = '{"ok":true}'
    ACCOUNT_NOT_FOUND = "Учетная запись не найдена"
    INSUFFICIENT_DATA_FOR_ACCOUNTING = "Недостаточно данных для входа"
    INSUFFICIENT_DATA_CREATE_USER = "Недостаточно данных для создания учетной записи"
    LOGIN_ALREADY_USAGE = "Этот логин уже используется. Попробуйте другой."
class DatailsUsers:
    datails_user = [
        ['Иван', 'Иванов', 'ул. Красная площадь, д. 3', '4', '+7950000000', '5', '2020-06-06',
         'Еду-уеду', "BLACK"],
        ['Семен', 'Семенов', 'ул. Площадь Революции, д. 36', '6', '+7950000001', '2', '2020-06-06',
         'Скоро буду', "GREY"],
        ['Мария', 'Петрова', 'ул. Комсомольская 58', '11', '+7950000002', '1', '2020-06-06',
         'Угнала тебя угнала', "BLACK"]
    ]
