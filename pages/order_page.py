import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OrderPage(BasePage):
    FIRST_NAME_INPUT = (By.XPATH, './/input[@placeholder="* Имя"]')
    LAST_NAME_INPUT = (By.XPATH, './/input[@placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_INPUT = (By.XPATH, './/input[@placeholder="* Станция метро"]')
    PHONE_INPUT = (By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, './/button[text()="Далее"]')

    DATE_INPUT = (By.XPATH, './/input[@placeholder="* Когда привезти самокат"]')
    RENT_PERIOD_DROPDOWN = (By.CLASS_NAME, 'Dropdown-placeholder')
    BLACK_COLOR_CHECKBOX = (By.ID, 'black')
    GREY_COLOR_CHECKBOX = (By.ID, 'grey')
    COMMENT_INPUT = (By.XPATH, './/input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, './/div[contains(@class, "Order_Buttons")]/button[text()="Заказать"]')
    CONFIRM_ORDER_BUTTON = (By.XPATH, './/button[text()="Да"]')
    SUCCESS_MODAL = (By.XPATH, './/div[contains(@class, "Order_ModalHeader") and contains(text(), "Заказ оформлен")]')

    def metro_station_option(self, station_name):
        return By.XPATH, f'.//div[contains(@class, "select-search__select")]//button[.//div[text()="{station_name}"]]'

    def rent_period_option(self, rent_period):
        return By.XPATH, f'.//div[contains(@class, "Dropdown-option") and text()="{rent_period}"]'

    @allure.step('Заполнить первую часть формы заказа')
    def fill_customer_info(self, first_name, last_name, address, metro_station, phone):
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
        self.send_keys(self.LAST_NAME_INPUT, last_name)
        self.send_keys(self.ADDRESS_INPUT, address)
        self.send_keys(self.METRO_INPUT, metro_station)
        self.click(self.metro_station_option(metro_station))
        self.send_keys(self.PHONE_INPUT, phone)
        self.click(self.NEXT_BUTTON)

    @allure.step('Заполнить вторую часть формы заказа')
    def fill_rent_info(self, date, rent_period, color, comment):
        self.send_keys(self.DATE_INPUT, date)
        self.driver.find_element(By.TAG_NAME, 'body').click()
        self.click(self.RENT_PERIOD_DROPDOWN)
        self.click(self.rent_period_option(rent_period))

        if color == 'black':
            self.click(self.BLACK_COLOR_CHECKBOX)
        elif color == 'grey':
            self.click(self.GREY_COLOR_CHECKBOX)

        self.send_keys(self.COMMENT_INPUT, comment)

    @allure.step('Подтвердить заказ')
    def submit_order(self):
        self.click(self.ORDER_BUTTON)
        self.click(self.CONFIRM_ORDER_BUTTON)

    @allure.step('Проверить отображение сообщения об успешном заказе')
    def is_success_modal_displayed(self):
        return self.find_visible_element(self.SUCCESS_MODAL).is_displayed()
