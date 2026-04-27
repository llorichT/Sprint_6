import allure

from pages.main_page import MainPage


@allure.epic('Яндекс.Самокат')
@allure.feature('Переходы по логотипам')
class TestRedirects:
    @allure.title('Переход на главную страницу Самоката по логотипу Самокат')
    def test_scooter_logo_redirects_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_top_order_button()

        main_page.click_scooter_logo()

        main_page.wait_url_contains('qa-scooter.praktikum-services.ru')
        assert main_page.get_current_url() == MainPage.BASE_URL

    @allure.title('Переход на главную страницу Дзена по логотипу Яндекса')
    def test_yandex_logo_opens_dzen_in_new_window(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        old_windows = main_page.get_window_handles()

        main_page.click_yandex_logo()
        main_page.wait_new_window_opened(old_windows)
        
        new_windows = main_page.get_window_handles()
        new_window = [window for window in new_windows if window not in old_windows][0]

        main_page.switch_to_window(new_window)
        main_page.wait_url_contains('dzen.ru')

        assert 'dzen.ru' in main_page.get_current_url()