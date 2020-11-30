import pytest
from one_hot_encoder import fit_transform


def test_list_str():
    """Тест поведения функции, если входным аргументом является список."""
    assert fit_transform(['Moscow', 'New York', 'Moscow', 'London']) == [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]


def test_args_str():
    """Тест поведения функции, если входные аргументы - строки."""
    assert fit_transform('Moscow', 'New York', 'Moscow', 'London') == [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]


def test_list_int():
    """Тест поведения функции, если входной аргумент - list[int]."""
    assert fit_transform([1, 2, 3, 3]) == [
        (1, [0, 0, 1]),
        (2, [0, 1, 0]),
        (3, [1, 0, 0]),
        (3, [1, 0, 0]),
    ]


def test_list_float():
    """Тест поведения функции, если входные аргументы типа float."""
    assert fit_transform([1.0, 2.5, 3.3, 3.7]) == [
        (1.0, [0, 0, 0, 1]),
        (2.5, [0, 0, 1, 0]),
        (3.3, [0, 1, 0, 0]),
        (3.7, [1, 0, 0, 0]),
    ]


def test_args_int():
    """Тест поведения функции, если входные аргументы типа int."""
    with pytest.raises(TypeError):
        fit_transform(1, 2, 3, 3)


def test_empty_list():
    """Тест поведения функции, если входной аргумент - пустой список"""
    assert fit_transform([]) == []


def test_empty_args():
    """Тест поведения функции, если 'len(args) == 0'"""
    with pytest.raises(TypeError):
        fit_transform()
