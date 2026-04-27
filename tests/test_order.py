import allure
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import FAQ_DATA, ORDER_DATA

@allure.epic('Яндекс.Самокат')
@allure.feature('Заказ самоката')
class TestOrder:
    @allure.title('Позитивный сценарий создания заказа')
    @pytest.mark.parametrize('order_data', ORDER_DATA)
    def test_create_order_successfully(self, driver, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open_main_page()

        if order_data['entry_point'] == 'top':
            main_page.click_top_order_button()
        else:
            main_page.click_bottom_order_button()

        order_page.fill_customer_info(
            order_data['first_name'],
            order_data['last_name'],
            order_data['address'],
            order_data['metro_station'],
            order_data['phone'],
        )
        order_page.fill_rent_info(
            order_data['date'],
            order_data['rent_period'],
            order_data['color'],
            order_data['comment'],
        )
        order_page.submit_order()

        assert order_page.is_success_modal_displayed()
