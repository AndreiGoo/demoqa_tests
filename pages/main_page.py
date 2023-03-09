from allure import step

from selenium.webdriver.common.by import By

from pages.layer import Layer


class MainPage(Layer):
    """Класс, предоставляющий методы для работы с главной страницей."""

    @step("Выбор категории на главной странице.")
    def choose_category(self, category: str) -> None:
        """
        Выбирает категорию.

        :param category: Название категории.
        """
        self.click(By.XPATH, self.element_by_text.format(category))
