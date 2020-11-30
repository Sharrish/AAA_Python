from one_hot_encoder import fit_transform
import unittest


class TestFitTransform(unittest.TestCase):
    """Класс для тестирования функции 'fit_transform' из one_hot_encoder.py."""

    def test_list_str(self):
        """Тест поведения функции, если входным аргументом является список."""
        actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]

        self.assertEqual(actual, expected)

    def test_args_str(self):
        """Тест поведения функции, если входные аргументы - строки."""
        actual = fit_transform('Moscow', 'New York', 'Moscow', 'London')
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]

        self.assertEqual(actual, expected)

    def test_list_int(self):
        """Тест поведения функции, если входной аргумент - list[int]."""
        # Несмотря, что функция объявлена как
        # def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
        # видим, что аргументами могут являться и не строки.
        actual = fit_transform([1, 2, 3, 3])
        expected = [
            (1, [0, 0, 1]),
            (2, [0, 1, 0]),
            (3, [1, 0, 0]),
            (3, [1, 0, 0]),
        ]

        self.assertEqual(actual, expected)

    def test_list_float(self):
        """Тест поведения функции, если входные аргументы типа float."""
        actual = fit_transform([1.0, 2.5, 3.3, 3.7])
        expected = [
            (1.0, [0, 0, 0, 1]),
            (2.5, [0, 0, 1, 0]),
            (3.3, [0, 1, 0, 0]),
            (3.7, [1, 0, 0, 0]),
        ]

        self.assertEqual(actual, expected)

    def test_args_int(self):
        """Тест поведения функции, если входные аргументы типа int."""
        # Попробуем не оборачивать в список и перехватить исключение TypeError
        with self.assertRaises(TypeError):
            fit_transform(1, 2, 3, 3)

    def test_not_in_result(self):
        """Проверяем, что в результате 'fit_transform' нет значения."""
        actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])

        self.assertNotIn(('Moscow', [1, 0, 0]), actual)

    def test_empty_list(self):
        """Тест поведения функции, если входной аргумент - пустой список"""
        actual = fit_transform([])
        expected = []

        self.assertEqual(actual, expected)

    def test_empty_args(self):
        """Тест поведения функции, если 'len(args) == 0'"""
        with self.assertRaises(TypeError):
            fit_transform()
