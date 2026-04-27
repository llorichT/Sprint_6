import allure
import pytest

from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

FAQ_DATA = [
    (0, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
    (1, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
    (2, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
    (3, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
    (4, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
    (5, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
    (6, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
    (7, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'),
]


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