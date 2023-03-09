from allure import step

from selenium.webdriver.common.by import By

from pages.layer import Layer


class ElementsPage(Layer):
    """Класс, предоставляющий методы для работы со страницей Elements."""

    @step("Выбор типа элемента.")
    def choose_type_element(self, type_element: str) -> None:
        """
        Выбирает тип элемента.

        :param type_element: Необходимый тип элемента.
        """
        self.click(By.XPATH, self.span_by_text.format(type_element))
