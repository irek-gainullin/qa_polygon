import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button

class EnterMarketplacePopup(BaseComponent):
    """
    Компонент попапа, где отображаются:
    - Кнопки входа
    - Ссылки на документацию
    - Заголовок Enter Marketplace
    """


    def __init__(self, page: Page):
        super().__init__(page)

        # Лого в левом верхнем угло
        self.text = Text(page,locator='/html/body/div[5]/div/div/div/div/div[1]/h3', name="Enter Marketplace text")
        # Кнопка входа в правом верхнем углу
        #self.enter_marketplace_button = Button(page, '/html/body/div[2]/header/div/div[2]/button',name="Enter Marketplace button")
