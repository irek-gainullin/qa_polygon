import uuid

import allure
import pytest
from playwright.sync_api import Playwright, Page, expect

from config import Settings
from pages.models_page import ModelsPage


@pytest.fixture
def chromium_page(playwright: Playwright, settings: Settings) -> Page:
    """
    Фикстура для запуска браузера Chromium и создания новой страницы.

    - Использует настройки из фикстуры `settings`.
    - Устанавливает глобальный таймаут ожиданий.
    - Включает запись видео и трейсинга (screenshots, snapshots, source).
    - После завершения теста:
        - сохраняет трейс в `settings.tracing_dir`;
        - прикрепляет видео и трейс к Allure-отчету;
        - закрывает браузер.

    :param playwright: Объект Playwright, предоставляемый pytest-playwright.
    :param settings: Настройки проекта.
    :yield: Новый объект `Page` для каждого теста.
    """
    expect.set_options(timeout=settings.expect_timeout)

    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(
        base_url=f"{settings.app_url}/",
        record_video_dir=settings.videos_dir
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    yield page

    tracing_file = settings.tracing_dir.joinpath(f'{uuid.uuid4()}.zip')
    context.tracing.stop(path=tracing_file)
    browser.close()

    allure.attach.file(tracing_file, name='trace', extension='zip')
    allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)


@pytest.fixture
def dashboard_page(chromium_page: Page) -> DashboardPage:
    """
    Фикстура для инициализации страницы дашборда.

    :param chromium_page: Страница браузера Chromium, созданная через фикстуру.
    :return: Объект `DashboardPage` для использования в тестах.
    """
    return DashboardPage(page=chromium_page)


@pytest.fixture
def registration_page(chromium_page: Page) -> RegistrationPage:
    """
    Фикстура для инициализации страницы регистрации.

    :param chromium_page: Страница браузера Chromium, созданная через фикстуру.
    :return: Объект `RegistrationPage` для использования в тестах.
    """
    return RegistrationPage(page=chromium_page)