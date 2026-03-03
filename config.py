from typing import Self

from pydantic import HttpUrl, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Конфигурация UI автотестов. Все значения загружаются из .env файла или переменных окружения.

    :param app_url: URL тестируемого приложения.
    :param headless: Флаг запуска браузера в headless-режиме.
    :param videos_dir: Путь к директории для сохранения видео.
    :param tracing_dir: Путь к директории для сохранения Playwright trace-файлов.
    :param expect_timeout: Таймаут ожиданий Playwright в миллисекундах.
    """

    model_config = SettingsConfigDict(
        env_file='.env',  # Загрузка переменных из файла .env
        env_file_encoding='utf-8',
        env_nested_delimiter='.'  # Позволяет использовать вложенные переменные, если потребуется
    )

    app_url: HttpUrl
    headless: bool
    videos_dir: DirectoryPath
    tracing_dir: DirectoryPath
    expect_timeout: float

    @classmethod
    def initialize(cls) -> Self:
        """
        Инициализирует экземпляр Settings. Если директории для видео и трейсинга не существуют — создаёт их.

        :return: Инициализированный объект Settings
        :raises ValueError: если директории не могут быть созданы или невалидны
        """
        videos_dir = DirectoryPath("./videos")
        tracing_dir = DirectoryPath("./tracing")

        videos_dir.mkdir(exist_ok=True)
        tracing_dir.mkdir(exist_ok=True)

        return Settings(videos_dir=videos_dir, tracing_dir=tracing_dir)