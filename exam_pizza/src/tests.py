# Запуск в терминале python3 -m pytest tests.py
# Для демонстрации coverage: python3 -m pytest tests.py --cov=click_for_pizza

import pytest
import random
from unittest.mock import patch  # для замены реального обращения к randint()
from click.testing import CliRunner  # для тестирования click
from pizza import Pepperoni, Hawaii, Margherita
from processes_with_pizza import bake, delivery, pickup
from click_for_pizza import menu, order


def test_dict():
    """Тест метода dict(self), возвращающего словарь рецепта."""
    excepted = {
        "🥟 dough": 500,
        "🧀 cheese": 125,
        "🥤 water": 125,
        "🍅 tomato sauce": 50,
        "🧂 salt": 20,
        "🍖 sausage": 200,
        "🌶 hot pepper": 20,
        "🧅 onion": 20,
    }

    assert Pepperoni(size="L").dict() == excepted


def test_size():
    """Тест того, что у для XL пицц всех ингредиентов в полтора раза больше."""
    hawaii_l_dict = Hawaii(size="L").dict()
    hawaii_xl_dict = Hawaii(size="XL").dict()
    for key in hawaii_l_dict:
        assert hawaii_xl_dict[key] == int(1.5 * hawaii_l_dict[key])


def test_str():
    """Тест метода str для рецепта пицц."""
    excepted = (
        "Pepperoni🍕 XL : 🥟 dough: 750г, 🧀 cheese: 187г, 🥤 water: "
        "187г, 🍅 tomato sauce: 75г, 🧂 salt: 30г, 🍖 sausage: 300г, "
        "🌶 hot pepper: 30г, 🧅 onion: 30г"
    )
    assert str(Pepperoni(size="XL")) == excepted


def test_eql():
    """Тест метода сравнения пицц с помощью равенства."""
    margherita_l1 = Margherita(size="L")
    margherita_l2 = Margherita(size="L")
    margherita_xl = Margherita(size="XL")
    pepperoni_xl = Pepperoni(size="XL")
    assert (
        margherita_l1 == margherita_l2
        and margherita_l1 != margherita_xl
        and margherita_xl != pepperoni_xl
    )


def test_orig_bake():
    """Тест функции bake, без применения декоратора."""
    original_bake = bake.__wrapped__
    assert original_bake(Hawaii(size="XL")) == "🍺 Приготовили"


def test_orig_delivery():
    """Тест функции delivery, без применения декоратора."""
    original_delivery = delivery.__wrapped__
    assert original_delivery(Margherita(size="XL")) == "🛵 Доставили"


def test_orig_pickup():
    """Тест функции pickup, без применения декоратора."""
    original_pickup = pickup.__wrapped__
    assert original_pickup(Pepperoni(size="XL")) == "🏡 Забрали"


def test_deco_bake_l():
    """Тест функции bake для пиццы размера L, после применения декоратора."""
    my_randint = 7
    # Вызываем randint() из random, заменив возвращаемое значение на my_randint
    with patch.object(random, "randint", return_value=my_randint):
        assert (
            bake(Pepperoni(size="L"))
            == "🍺 Приготовили Pepperoni🍕 L за ⌚ 7мин!"
        )


def test_deco_bake_xl():
    """Тест функции bake для пиццы размера XL, после применения декоратора."""
    my_randint = 7
    # Вызываем randint() из random, заменив возвращаемое значение на my_randint
    with patch.object(random, "randint", return_value=my_randint):
        assert (
            bake(Pepperoni(size="XL"))
            == "🍺 Приготовили Pepperoni🍕 XL за ⌚ 14мин!"
        )


def test_deco_delivery():
    """Тест функции delivery, после применения декоратора."""
    my_randint = 10
    # Вызываем randint() из random, заменив возвращаемое значение на my_randint
    with patch.object(random, "randint", return_value=my_randint):
        assert (
            delivery(Margherita(size="L"))
            == "🛵 Доставили Margherita🧀 L за ⌚ 10мин!"
        )


def test_deco_pickup():
    """Тест функции pickup, после применения декоратора."""
    my_randint = 9
    # Вызываем randint() из random, заменив возвращаемое значение на my_randint
    with patch.object(random, "randint", return_value=my_randint):
        assert pickup(Hawaii(size="XL")) == "🏡 Забрали Hawaii🍍 XL за ⌚ 9мин!"


def test_menu():
    """Тест вывода 😋 меню пиццерии."""
    runner = CliRunner()
    result = runner.invoke(menu)
    assert result.exit_code == 0
    actual = result.output
    assert (
        "😋 Наше меню 😋" in actual
        and "-Pepperoni🍕 L" in actual
        and "-Margherita🧀 XL" in actual
    )


def test_order_delivery():
    """Тест функции order - вывода процесса
    приготовления и 🛵 доставки пиццы."""
    runner = CliRunner()
    my_randint = 5
    # Вызываем randint() из random, заменив возвращаемое значение на my_randint
    with patch.object(random, "randint", return_value=my_randint):
        result = runner.invoke(order, ["pepperoni", "l", "--delivery"])
        assert result.exit_code == 0
        actual = result.output
        excepted = (
            "🍺 Приготовили Pepperoni🍕 L за ⌚ 5мин!\n"
            "🛵 Доставили Pepperoni🍕 L за ⌚ 5мин!\n"
        )
        assert actual == excepted


def test_order_pickup():
    """Тест функции order - вывода процесса
    приготовления и 🏡 самовывоза пиццы."""
    runner = CliRunner()
    my_randint = 7
    # Вызываем randint() из random, заменив возвращаемое значение на my_randint
    with patch.object(random, "randint", return_value=my_randint):
        result = runner.invoke(order, ["hawaii", "xl"])
        assert result.exit_code == 0
        actual = result.output
        excepted = (
            "🍺 Приготовили Hawaii🍍 XL за ⌚ 14мин!\n"
            "🏡 Забрали Hawaii🍍 XL за ⌚ 7мин!\n"
        )
        assert actual == excepted
