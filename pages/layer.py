from allure import step

from pages.base import BasePageObject


class Layer(BasePageObject):
    """Класс-посредник, хранящий шаблоны локаторов элементов и общие методы для работы со страницами."""

    """Шаблоны локаторов элементов."""
    element_by_text = "//*[text()='{}']"
    span_by_text = "//span[text()='{}']"

    @step("Проверка, что открыта требуемая страница сайта.")
    def check_url(self, url: str) -> bool:
        """
        Проверяет, что открыта требуемая страница сайта.

        :param url:  Требуемая страница сайта.
        """
        return self.get_url() == url
