from dataclasses import dataclass


@dataclass
class CheckBoxLocators:
    """Класс, хранящий уникальные шаблоны локаторов элементов страницы Check Box."""

    directories_button: str = "//span[text()='{}']/../../button"
    directory_icon: str = "//span[text()='{}']/../..//span[@class='rct-node-icon']/*[name()='svg']"
    check_box_icon: str = "//span[text()='{}']/../span[@class='rct-checkbox']//*[name()='svg']"


@dataclass
class CheckBoxDirectories:
    """Класс, хранящий названия директорий со страницы Check Box."""

    home: str = "Home"
    desktop: str = "Desktop"
    documents: str = "Documents"
    downloads: str = "Downloads"


@dataclass
class CheckBoxFiles:
    """Класс, хранящий названия файлов со страницы Check Box."""

    word_file: str = "Word File.doc"


@dataclass
class CheckBoxMessageFiles:
    """Класс, хранящий названия файлов из сообщения о выборе со страницы Check Box."""

    word_file: str = "wordFile"
