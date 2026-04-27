import allure
import pytest

from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import FAQ_DATA, ORDER_DATA

@allure.epic('Яндекс.Самокат')
@allure.feature('FAQ')
class TestFAQ:
    @allure.title('Проверка текста ответа в разделе Вопросы о важном')
    @pytest.mark.parametrize('question_index, expected_answer', FAQ_DATA)
    def test_faq_answer_text_is_correct(self, driver, question_index, expected_answer):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.open_faq_question(question_index)
        actual_answer = main_page.get_faq_answer_text(question_index)

        assert actual_answer == expected_answer