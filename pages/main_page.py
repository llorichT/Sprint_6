import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/'

    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')
    TOP_ORDER_BUTTON = (By.XPATH, './/button[@class="Button_Button__ra12g"]')
    BOTTOM_ORDER_BUTTON = (By.XPATH, './/button[contains(@class, "Button_Middle__1CSJM") and text()="Заказать"]')
    SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')

    FAQ_QUESTIONS = [
        (By.ID, 'accordion__heading-0'),
        (By.ID, 'accordion__heading-1'),
        (By.ID, 'accordion__heading-2'),
        (By.ID, 'accordion__heading-3'),
        (By.ID, 'accordion__heading-4'),
        (By.ID, 'accordion__heading-5'),
        (By.ID, 'accordion__heading-6'),
        (By.ID, 'accordion__heading-7'),
    ]

    FAQ_ANSWERS = [
        (By.ID, 'accordion__panel-0'),
        (By.ID, 'accordion__panel-1'),
        (By.ID, 'accordion__panel-2'),
        (By.ID, 'accordion__panel-3'),
        (By.ID, 'accordion__panel-4'),
        (By.ID, 'accordion__panel-5'),
        (By.ID, 'accordion__panel-6'),
        (By.ID, 'accordion__panel-7'),
    ]

    @allure.step('Открыть главную страницу')
    def open_main_page(self):
        self.open(self.BASE_URL)
        self.accept_cookies_if_visible()

    @allure.step('Принять cookies, если баннер отображается')
    def accept_cookies_if_visible(self):
        try:
            self.click(self.COOKIE_BUTTON)
        except Exception:
            pass

    @allure.step('Нажать верхнюю кнопку Заказать')
    def click_top_order_button(self):
        self.click(self.TOP_ORDER_BUTTON)

    @allure.step('Нажать нижнюю кнопку Заказать')
    def click_bottom_order_button(self):
        self.scroll_to_element(self.BOTTOM_ORDER_BUTTON)
        self.click(self.BOTTOM_ORDER_BUTTON)

    @allure.step('Открыть вопрос FAQ с индексом {index}')
    def open_faq_question(self, index):
        question_locator = self.FAQ_QUESTIONS[index]
        self.scroll_to_element(question_locator)
        element = self.find_element(question_locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Получить текст ответа FAQ с индексом {index}')
    def get_faq_answer_text(self, index):
        return self.get_text(self.FAQ_ANSWERS[index])

    @allure.step('Кликнуть по логотипу Самоката')
    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    @allure.step('Кликнуть по логотипу Яндекса')
    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)
