from keyword import iskeyword


class ObjectTransformator:
    """Класс, ĸоторый преобразовывает JSON-объеĸты в python-объеĸты с
    доступом ĸ атрибутам(в том числе вложенным) через точĸу (класс
    используется в классе Advert)."""

    def __init__(self, mapping: dict):
        if not isinstance(mapping, dict):
            raise ValueError("mapping должен быть экземпляром dict")
        for key, value in mapping.items():
            if iskeyword(key):
                key += "_"
            if isinstance(value, dict):
                self.__dict__[key] = ObjectTransformator(value)
            else:
                self.__dict__[key] = value

    def __repr__(self):
        return str(self.__dict__)


class ColorizeMixin:
    def __init__(self, style=1, text_color=32, background_color=43):
        self.style = style
        self.text_color = text_color
        self.background_color = background_color

    def __str__(self):
        return (
            "\033[{style};{repr_color_code};{background_color}m{text}"
            "{ENDC}".format(
                style=self.style,
                repr_color_code=self.text_color,
                background_color=self.background_color,
                text=self.__repr__(),
                ENDC="\033[m",  # reset to the defaults
            )
        )


class Advert(ColorizeMixin):
    """Класс, который из объявления в формате JSON создает экземпляр класса
    со всеми соответсвующими атрибутами, которые не являюятся атрибутами
    класса и досутпны через точку.
    title - обязательное поле объявления."""

    def __init__(self, mapping: dict):
        ColorizeMixin.__init__(self)
        mapping_transformed = ObjectTransformator(mapping).__dict__
        if "title" not in mapping_transformed:
            raise ValueError("Объявление должно содержать поле 'title'")
        if "price" in mapping_transformed:
            self.price = mapping_transformed["price"]
        self.__dict__.update(mapping_transformed)

    def __repr__(self):
        return f"{self.title} | {self.price} ₽"

    @property
    def price(self):
        if "price" not in self.__dict__:
            return 0
        else:
            return self.__dict__["price"]

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("price must be >= 0")
        self._price = new_price
