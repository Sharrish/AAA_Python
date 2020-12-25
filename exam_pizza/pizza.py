from typing import Literal, Dict


SizePizza = Literal["L", "XL"]  # для typing размера пиццы


class Pizza:
    """🍕Базовый класс для пицц🍕."""

    # Базовые ингридиенты для всех пицц
    recipe_base = {
        "🥟 dough": 500,
        "🧀 cheese": 125,
        "🥤 water": 125,
        "🍅 tomato sauce": 50,
        "🧂 salt": 20,
    }

    def __init__(self, name: str, size: SizePizza, recipe: Dict[str, int]):
        self.__dict__.update(self.recipe_base)  # базовые ингридиенты
        self.__dict__.update(recipe)  # ингридиенты отдельной пиццы

        if size == "XL":  # большая пицца в полтора раза больше
            for key in self.__dict__:
                self.__dict__[key] = int(1.5 * self.__dict__[key])

        self.name = "{name} {size}".format(name=name, size=size)
        self.size = size

    def dict(self) -> Dict:
        """Выводит рецепт в виде словаря."""
        recipe = self.__dict__.copy()
        recipe.pop("name")
        recipe.pop("size")
        return recipe

    def __eq__(self, other) -> bool:
        """Сравнение пицц."""
        return self.dict() == other.dict()

    def __str__(self) -> str:
        recipe_str = ", ".join(
            [
                "{}: {}г".format(key, value)
                for key, value in self.dict().items()
            ]
        )

        return "{}: {}".format(self.name.ljust(14, " "), recipe_str)


class Pepperoni(Pizza):
    """Класс для пиццы 'Пепперони'🍕."""

    name = "Pepperoni🍕"
    recipe = {
        "🍖 sausage": 200,
        "🌶 hot pepper": 20,
        "🧅 onion": 20,
    }

    def __init__(self, size):
        super().__init__(self.name, size, self.recipe)


class Margherita(Pizza):
    """Класс для пиццы 'Маргарита'🧀."""

    name = "Margherita🧀"
    recipe = {
        "🧀 mozzarella": 100,
        "🧀 parmesan": 75,
        "🍅 tomato": 70,
        "🥬 basil": 15,
    }

    def __init__(self, size):
        super().__init__(self.name, size, self.recipe)


class Hawaii(Pizza):
    """Класс для Гавайской пиццы🍍."""

    name = "Hawaii🍍"
    recipe = {
        "🍍 pineapple": 150,
        "🥓 bacon": 125,
        "🥑 olive oil": 15,
        "🥬 basil": 15,
    }

    def __init__(self, size):
        super().__init__(self.name, size, self.recipe)


# if __name__ == '__main__':
#     print(Pepperoni(size="L").dict())
#     print(str(Pepperoni(size="XL")))
