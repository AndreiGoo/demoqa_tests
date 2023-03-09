from dataclasses import dataclass


@dataclass
class MainPageCategories:
    """Класс, хранящий названия категорий на главной странице."""

    elements: str = "Elements"
