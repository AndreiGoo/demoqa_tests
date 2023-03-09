from allure import title
from allure import severity

from pages.main_page import MainPage
from pages.elements_page import ElementsPage
from pages.check_box_page import CheckBoxPage

from data.tests_data import Routes
from data.main_page_data import MainPageCategories
from data.elements_page_data import TypesElements
from data.check_box_page_data import CheckBoxDirectories, CheckBoxFiles, CheckBoxMessageFiles


@title("Тесткейс 1.0")
@severity("Normal")
def test_demoqa(driver):
    main_page = MainPage(driver)
    assert main_page.check_url(Routes.main_page), "Сайт https://demoqa.com/ не открыт."

    main_page.choose_category(MainPageCategories.elements)
    assert main_page.check_url(Routes.main_page + Routes.elements_page), "Страница Elements не открыта."

    elements_page = ElementsPage(driver)
    elements_page.choose_type_element(TypesElements.check_box)
    assert elements_page.check_url(Routes.main_page + Routes.checkbox), "Страница Check Box не открыта."

    check_box_page = CheckBoxPage(driver)
    check_box_page.choose_directory(CheckBoxDirectories.home)
    assert check_box_page.check_directory_opened(CheckBoxDirectories.home), "Директория Home не раскрыта."

    check_box_page.choose_directory(CheckBoxDirectories.downloads)
    assert check_box_page.check_directory_opened(CheckBoxDirectories.downloads), "Директория Downloads не раскрыта."

    check_box_page.choose_check_box(CheckBoxFiles.word_file)
    assert check_box_page.check_check_box_selected(CheckBoxFiles.word_file), "Чекбокс файла Word File.doc не выбран."
    assert check_box_page.check_selection_message(CheckBoxMessageFiles.word_file), \
        "Сообщение 'You have selected:' не появилось"
