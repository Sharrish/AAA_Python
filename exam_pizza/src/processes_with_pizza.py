from typing import Callable
from functools import wraps
import random
from pizza import Pizza

# from pizza import Hawaii


def log(str_for_print: str) -> Callable:
    """Параметрический декоратор, в котором параметр
    шаблон - название процесса и время его выполения.
    Параметры шаблона: название процесса, названеие пиццы, время выолнения."""

    def deco(process: Callable) -> Callable:
        """Простой декоратор."""

        @wraps(process)  # магия, чтобы не менялось имя декорируемой функции
        def get_str_for_print(pizza: Pizza) -> str:
            """Возвращает строку, полученную после подстановки значений в
            шаблон декоратора log."""
            process_name = process(pizza)
            process_time = random.randint(5, 10)

            # Большую пиццу дольше готовить
            if process.__name__ == "bake" and pizza.size == "XL":
                process_time *= 2

            return str_for_print.format(process_name, pizza.name, process_time)

        return get_str_for_print

    return deco


@log("{} {} за ⌚ {}мин!")
def bake(pizza: Pizza) -> str:
    """Возвращает сообщение о готовке пиццы."""
    return "🍺 Приготовили"


@log("{} {} за ⌚ {}мин!")
def delivery(pizza: Pizza) -> str:
    """Возвращает сообщение о доставке пиццы."""
    return "🛵 Доставили"


@log("{} {} за ⌚ {}мин!")
def pickup(pizza: Pizza) -> str:
    """Возвращает сообщение о самовывозе пиццы."""
    return "🏡 Забрали"


# if __name__ == '__main__':
#     original_bake = bake.__wrapped__
#     original_delivery = delivery.__wrapped__
#     original_pickup = pickup.__wrapped__
#     print(original_bake(Hawaii(size="XL")))
#     print(original_delivery(Hawaii(size="XL")))
#     print(original_pickup(Hawaii(size="XL")))
#
#     print(bake(Hawaii(size="XL")))
#     print(delivery(Hawaii(size="XL")))
#     print(pickup(Hawaii(size="XL")))
