import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.image import Image
from elements.button import Button


class HeaderNavbar(BaseComponent):
    """
    Компонент верхнего меню (navbar), где отображаются:
    - Лого Супера
    - Несколько пунктов меню (потом)
    - Кнопка входа/логин пользователя
    """

    def __init__(self, page: Page):
        super().__init__(page)

        # Лого в левом верхнем угло
        self.logo = Image(page, 'logo',name="Marketplace logo")
        # Кнопка входа в правом верхнем углу
        self.enter_marketplace_button = Button(page, '/html/body/div[2]/header/div/div[2]/button',name="Enter Marketplace button")

    @allure.step("Check visible navbar")
    def check_visible(self):
        """
        Проверяет, что navbar отображается корректно:
        - Название приложения видно и соответствует 'UI Course'
        - Приветствие содержит имя пользователя
        """
        self.logo.check_visible()

        self.enter_marketplace_button.check_visible()
        self.enter_marketplace_button.check_have_text(f'Enter Marketplace')