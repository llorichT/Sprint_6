import allure
from selenium.webdriver.common.by import By

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    def metro_station_option(self, station_name):
        return By.XPATH, f'.//div[contains(@class, "select-search__select")]//button[.//div[text()="{station_name}"]]'

    def rent_period_option(self, rent_period):
        return By.XPATH, f'.//div[contains(@class, "Dropdown-option") and text()="{rent_period}"]'

    @allure.step('Заполнить первую часть формы заказа')
    def fill_customer_info(self, first_name, last_name, address, metro_station, phone):
        self.send_keys(OrderPageLocators.FIRST_NAME_INPUT, first_name)
        self.send_keys(OrderPageLocators.LAST_NAME_INPUT, last_name)
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)
        self.send_keys(OrderPageLocators.METRO_INPUT, metro_station)
        self.click(self.metro_station_option(metro_station))
        self.send_keys(OrderPageLocators.PHONE_INPUT, phone)
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить вторую часть формы заказа')
    def fill_rent_info(self, date, rent_period, color, comment):
        self.send_keys(OrderPageLocators.DATE_INPUT, date)
        self.driver.find_element(By.TAG_NAME, 'body').click()
        self.click(OrderPageLocators.RENT_PERIOD_DROPDOWN)
        self.click(self.rent_period_option(rent_period))

        if color == 'black':
            self.click(OrderPageLocators.BLACK_COLOR_CHECKBOX)
        elif color == 'grey':
            self.click(OrderPageLocators.GREY_COLOR_CHECKBOX)

        self.send_keys(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step('Подтвердить заказ')
    def submit_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step('Проверить отображение сообщения об успешном заказе')
    def is_success_modal_displayed(self):
        return self.find_visible_element(OrderPageLocators.SUCCESS_MODAL).is_displayed()