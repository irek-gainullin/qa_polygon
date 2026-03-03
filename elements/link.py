from elements.base_element import BaseElement


class Link(BaseElement):
    """
    Класс для работы с ссылками на странице.
    Наследует все основные методы от BaseElement, предоставляя возможность
    работать с ссылками как элементами на странице.
    """

    @property
    def type_of(self) -> str:
        """
        Возвращает тип элемента. В случае ссылки возвращается "link".
        """
        return "link"