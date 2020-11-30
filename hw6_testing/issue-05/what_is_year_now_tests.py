import unittest
from unittest.mock import patch  # для замены реального обращения к API
from what_is_year_now import what_is_year_now
import urllib.request
import io


class TestWhatIsYearNow(unittest.TestCase):
    """Тестирование функции 'what_is_year_now()' из what_is_year_now.py."""

    def test_separator_dash(self):
        """Тест, проверяющий поведение функции, при дате, заданной в
        формате 'YYYY-MM-DD'."""
        dict_for_json = '{"currentDateTime": "2020-01-01"}'

        # Вызываем urlopen из urllib.request, заменив возвращаемое значение
        # на 'файл' c dict_for_json, к которому в функции применяется json.load
        with patch.object(urllib.request, "urlopen",
                          return_value=io.StringIO(dict_for_json)):
            actual = what_is_year_now()
        expected = 2020
        self.assertEqual(actual, expected)

    def test_separator_point(self):
        """Тест, проверяющий поведение функции, при дате, заданной в
        формате 'DD.MM.YYYY'."""
        dict_for_json = '{"currentDateTime": "01.01.2020"}'

        with patch.object(urllib.request, "urlopen",
                          return_value=io.StringIO(dict_for_json)):
            actual = what_is_year_now()
        expected = 2020
        self.assertEqual(actual, expected)

    def test_incomplete_data(self):
        """Тест, в котором не сумеем обратится к datetime_str[DMY_SEP_INDEX]"""
        dict_for_json = '{"currentDateTime": "2020"}'

        with patch.object(urllib.request, "urlopen",
                          return_value=io.StringIO(dict_for_json)):
            with self.assertRaises(IndexError):
                what_is_year_now()

    def test3(self):
        """Тест, проверяющий поведение функции, при дате, заданной в
        формате 'DD:MM:YYYY'."""
        dict_for_json = '{"currentDateTime": "01:03:2020"}'

        with patch.object(urllib.request, "urlopen",
                          return_value=io.StringIO(dict_for_json)):
            with self.assertRaises(ValueError):
                what_is_year_now()
