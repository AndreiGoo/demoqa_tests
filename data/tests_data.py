from dataclasses import dataclass


@dataclass
class Routes:
    """Класс, хранящий адреса страниц."""

    main_page: str = "https://demoqa.com/"
    elements_page: str = "elements"
    checkbox: str = "checkbox"
