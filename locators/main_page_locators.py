from selenium.webdriver.common.by import By


class MainPageLocators:
    
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