from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_c
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BasePageObject:
    """Класс, предоставляющий методы для работы с драйвером браузера."""

    def __init__(self, driver):
        """
        Инициализация драйвера.
        """
        self.driver = driver

    def wait_visibility(self, by: By, locator: str, timeout: int = 10) -> WebElement:
        """
        Ожидает видимости элемента на экране, затем возвращает его.

        :param by: Метод поиска локатора.
        :param locator: Локатор элемента.
        :param timeout: Время ожидания в секундах.
        """
        return WebDriverWait(self.driver, timeout).until(e_c.visibility_of_element_located((by, locator)))

    def click(self, by: By, locator: str, timeout: int = 10) -> None:
        """
        Ожидает возможности кликнуть по элементу, затем кликает на него.

        :param by: Метод поиска локатора.
        :param locator: Локатор элемента.
        :param timeout: Время ожидания в секундах.
        """
        WebDriverWait(self.driver, timeout).until(e_c.element_to_be_clickable((by, locator))).click()

    def get_url(self) -> str:
        """
        Возвращает адрес текущей страницы в браузере.
        """
        return self.driver.current_url

    def wait_located(self, by: By, locator: str, timeout: int = 10) -> WebElement:
        """
        Ожидает появления элемента в DOM, затем возвращает его.

        :param by: Стратегия поиска.
        :param locator: Локатор элемента.
        :param timeout: Время ожидания в секундах.
        """
        return WebDriverWait(self.driver, timeout).until(e_c.presence_of_element_located((by, locator)))
