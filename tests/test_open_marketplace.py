import allure
import pytest

from pages.models_page import ModelsPage
from tools.routes import AppRoute


class TestOpenMarketplace:
    @allure.title("Successful page open")
    def test_open_marketplace_page(
            self,
            models_page: ModelsPage
    ):
        # 1. Переход на страницу моделей
        models_page.visit(AppRoute.MODELS)

        # 2. Проверка, что форма регистрации отображается
        models_page.header_navbar.logo.check_visible()

        # 3. Проверка что отображается кнопка Enter Marketplace
        #models_page.header_navbar.enter_marketplace_button.check_visible()

        #4. Клик по кнопке регистрации
        #models_page.header_navbar.enter_marketplace_button.click()

        # 5. Проверка отображения элементов на Dashboard
        #models_page.enter_marketplace_popup.text.check_visible()