import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/'

    @allure.step('Открыть главную страницу')
    def open_main_page(self):
        self.open(self.BASE_URL)
        self.accept_cookies_if_visible()

    @allure.step('Принять cookies, если баннер отображается')
    def accept_cookies_if_visible(self):
        try:
            self.click(MainPageLocators.COOKIE_BUTTON)
        except Exception:
            pass

    @allure.step('Нажать верхнюю кнопку Заказать')
    def click_top_order_button(self):
        self.click(MainPageLocators.TOP_ORDER_BUTTON)

    @allure.step('Нажать нижнюю кнопку Заказать')
    def click_bottom_order_button(self):
        self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.click(MainPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step('Открыть вопрос FAQ с индексом {index}')
    def open_faq_question(self, index):
        question_locator = MainPageLocators.FAQ_QUESTIONS[index]
        self.scroll_to_element(question_locator)
        element = self.find_element(question_locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Получить текст ответа FAQ с индексом {index}')
    def get_faq_answer_text(self, index):
        return self.get_text(MainPageLocators.FAQ_ANSWERS[index])

    @allure.step('Кликнуть по логотипу Самоката')
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Кликнуть по логотипу Яндекса')
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)