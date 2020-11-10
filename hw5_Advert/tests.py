import json
from advert import Advert


def test1():
    """Тест поведения класса Advert в случае отсутствия поля title."""
    lesson_str = """{
        "price": 100,
        "location":
            {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
            }
        }"""
    lesson = json.loads(lesson_str)
    try:
        lesson_ad = Advert(lesson)
        print(lesson_ad)
    except ValueError:
        print(
            "Тест1 поведения класса Advert в случае отсутствия поля title "
            "прошел успешно!"
        )


def test2():
    """Тест поведения класса Advert, проверяющий обращение к атрибуту через
    точку."""
    lesson_str = """{
    "title": "python",
    "price": 0,
    "location":
        {
        "address": "город Москва, Лесная, 7",
        "metro_stations": ["Белорусская"]
        }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    assert lesson_ad.location.address == "город Москва, Лесная, 7"
    print(
        "Тест2 поведения класса Advert, проверяющий обращение к атрибуту "
        "через точку прошел успешно!"
    )


def test3():
    """Тест поведения класса Advert при попытке задания price < 0."""
    lesson_str = '{"title": "python", "price": -1}'
    lesson = json.loads(lesson_str)
    try:
        lesson_ad = Advert(lesson)
        print(lesson_ad)
    except ValueError:
        print(
            "Тест3 поведения класса Advert при попытке задания price < 0 "
            "прошел успешно!"
        )


def test4():
    """Тест поведения класса Advert в случае обращения к отсутсвующему полю
    price."""
    lesson_str = '{"title": "python"}'
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    assert lesson_ad.price == 0
    print(
        "Тест4 поведения класса Advert в случае обращения к отсутсвующему "
        "полю price прошел успешно!"
    )


def test5():
    """Тест поведения класса Advert в случае, если атрибуты являются
    ключевыми словами языка Python."""
    lesson_str = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
            "address": "поселение Ельдигинское, поселок санатория Тишково, 25"
        }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    assert lesson_ad.class_ == "dogs"
    print(
        "Тест5 поведения класса Advert в случае, если атрибуты являются "
        "ключевыми словами прошел успешно!"
    )


def test6():
    """Тест на цветное отображение экземпляра класса Advert."""
    lesson_str = '{"title": "python", "price": 100, "location": "Moscow"}'
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(
        "Тест6 на цветное отображение экземпляра класса Advert: {} прошел "
        "успешно!".format(lesson_ad)
    )


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
