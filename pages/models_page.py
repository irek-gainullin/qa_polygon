import re

from playwright.sync_api import Page

from elements.button import Button
from elements.image import Image
from pages.base_page import BasePage
from components.header_navbar import HeaderNavbar
from components.enter_marketplace_popup import EnterMarketplacePopup


class ModelsPage(BasePage):
    """
    Страница регистрации (Registration Page).

    Включает элементы:
    - Форма регистрации
    - Кнопка для перехода на страницу входа
    - Кнопка для отправки формы регистрации

    Наследуется от BasePage.
    """

    def __init__(self, page: Page):
        """
        Инициализация страницы регистрации.

        :param page: Экземпляр страницы Playwright
        """
        super().__init__(page)

        # Компоненты страницы
        self.header_navbar = HeaderNavbar(page)  # Хедер
        self.enter_marketplace_popup = EnterMarketplacePopup(page)

        # Элементы страницы
        self.logo = Image(page, "logo", "SuperProtocol Logo")  # Ссылка на страницу входа
        self.enter_marketplace_button = Button(page, "/html/body/div[2]/header/div/div[2]/button",
                                          "Enter Marketplace Button")  # Кнопка отправки формы
    def click_enter_marketplace_button(self):
        """
        Клик на кнопку "Enter Marketplace" и проверка открытия попапа.

        :raises AssertionError: Если URL не соответствует ожидаемому
        """
        # Нажатие на кнопку Входа в маркетплейс
        self.enter_marketplace_button.check_visible()
        self.enter_marketplace_button.check_visible()
        # Проверка, что мы перенаправлены на страницу панели управления
        #self.check_current_url(re.compile(".*/#/dashboard"))

    def check_logo_is_visible(self):

        self.logo.check_visible()
        self.logo.click()
        self.check_current_url(re.compile(".*/marketplace/models"))

    def check_popup_text_is_visible(self):
        self.enter_marketplace_popup.text.check_visible()