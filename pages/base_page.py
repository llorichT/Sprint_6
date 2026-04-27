import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    @allure.step('Открыть страницу: {url}')
    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_visible_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def find_clickable_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step('Кликнуть по элементу')
    def click(self, locator):
        self.find_clickable_element(locator).click()

    def send_keys(self, locator, value):
        element = self.find_visible_element(locator)
        element.clear()
        element.send_keys(value)

    def get_text(self, locator):
        return self.find_visible_element(locator).text

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center"});', element)
        return element

    def wait_url_contains(self, text):
        WebDriverWait(self.driver, self.timeout).until(EC.url_contains(text))

    def wait_new_window_opened(self, old_windows):
        WebDriverWait(self.driver, self.timeout).until(EC.new_window_is_opened(old_windows))