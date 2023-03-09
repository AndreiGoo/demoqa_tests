from allure import step

from selenium.webdriver.common.by import By

from pages.layer import Layer

from data.check_box_page_data import CheckBoxLocators


class CheckBoxPage(Layer):
    """Класс, предоставляющий методы для работы со страницей Check Box."""

    @step("Выбор директории.")
    def choose_directory(self, directory: str) -> None:
        """
        Выбирает директорию.

        :param directory: Название директории.
        """
        self.click(By.XPATH, CheckBoxLocators.directories_button.format(directory))

    @step("Проверка, что директория раскрыта.")
    def check_directory_opened(self, directory: str) -> bool:
        """
        Проверяет, что директория раскрыта.

        :param directory: Название директории.
        """
        return self.wait_located(By.XPATH, CheckBoxLocators.directory_icon.format(directory)).get_attribute(
            "class").count("open") > 0

    @step("Выбор чекбокса.")
    def choose_check_box(self, object_name: str) -> None:
        """
        Выбирает чекбокс объекта.

        :param object_name: Название объекта, чей чекбокс надо выбрать.
        """
        self.click(By.XPATH, CheckBoxLocators.check_box_icon.format(object_name))

    @step("Проверка чекбокса.")
    def check_check_box_selected(self, object_name: str) -> bool:
        """
        Проверяет, что чекбокс объекта выбран.

        :param object_name: Название объекта, чей чекбокс должен быть выбран.
        """
        return self.wait_located(By.XPATH, CheckBoxLocators.check_box_icon.format(object_name)).get_attribute(
            "class").count("icon-check") > 0

    @step("Проверка сообщения о выбранных файлах")
    def check_selection_message(self, *files: str) -> bool:
        """
        Проверяет, что сообщение о выбранных файлах отображается.

        :param files: Файлы, которые должны быть выбраны.
        """
        if self.wait_visibility(By.XPATH, self.span_by_text.format("You have selected :")).is_displayed():
            for file in files:
                if not self.wait_visibility(By.XPATH, self.span_by_text.format(file)).is_displayed():
                    return False
            return True
