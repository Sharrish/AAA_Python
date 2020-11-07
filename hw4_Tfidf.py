import re
from typing import List
from collections import Counter
from copy import deepcopy
from math import log


# Задание #1: count vectorizer
# Реализуйте класс CountVectorizer, имеющий метод fit_transform
class CountVectorizer:
    """Класс для построения мешка слов(матрицы встречаймости слов в
    документах корпуса)."""

    def __init__(self, lowercase: bool = True, clear: bool = True):
        self.lowercase = lowercase
        self.clear = clear
        self.vocabulary = []
        self.count_matrix = []

    def preprocess(self, corpus: List[str]):
        """Проводит препроцессинг корпуса - приведение всех экземпляров к
        нижнему регистру и удаление всех небуквенных символов,
        кроме пробелов."""
        if self.lowercase:  # приведение к нижнему регистру
            for i in range(len(corpus)):
                corpus[i] = corpus[i].lower()
        if self.clear:  # удаление всех небуквенных символов, кроме пробелов
            for i in range(len(corpus)):
                # whitespace characters -> ' '
                corpus[i] = re.sub(r"\s", " ", corpus[i])
                # Несколько пробелов в один
                corpus[i] = re.sub(r" +", " ", corpus[i])
                # Оставляем только буквы и пробелы:
                corpus[i] = re.sub(r"[^A-Za-zА-Яа-я ]", "", corpus[i])

    def tokeniser(self, corpus: List[str]):
        """Проводит токенизацию корпуса по всем whitespace символам."""
        # str.split() without an argument splits on whitespace:
        for i in range(len(corpus)):
            corpus[i] = corpus[i].split()

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """Создаёт копию корпуса пользователя, для которого выполняет
        препроцессинг и токенизацию вычисляя словарь для всего корпуса и
        матрицу встречаймости слов в документах корпуса."""
        copy_corpus = deepcopy(corpus)  # чтобы corpus пользователя не менялся
        self.preprocess(copy_corpus)
        self.tokeniser(copy_corpus)
        counter = Counter()
        for d in copy_corpus:
            counter.update(d)
        self.vocabulary = list(counter.keys())
        for d in copy_corpus:
            counter = Counter(d)
            one_hot_vector = [counter[word] for word in self.vocabulary]
            self.count_matrix.append(one_hot_vector)
        return self.count_matrix

    def get_feature_names(self) -> List[str]:
        """Возвращает все слова, которые встречаются в корпусе."""
        return self.vocabulary


def test_task1():
    """Функция для тестирования класса CountVectorizer"""
    print("-----Тест для класса CountVectorizer-----", end="\n\n")
    corpus = [
        "Crock Pot, Pasta55 Never boil& pasta? again",
        "Pasta Pomodoro Fresh 6ingredients6     Parmesan to taste!",
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    # Проверяем, что corpus пользователя не изменился
    print("Корпус пользователя:\n{}".format(corpus), end="\n\n")
    print("Словарь:\n{}".format(vectorizer.get_feature_names()), end="\n\n")
    print("Мешок слов:\n{}".format(count_matrix))
    print("-" * 100, end="\n\n")


# Задание #2: term frequency
# Реализуйте функцию tf_transform
def tf_transform(count_matrix: List[List[int]]) -> List[List[float]]:
    """По матрице встречаймости слов в документах корпуса(count_matrix)
    возвращает матрицу отношений числа вхождений некоторого слова к общему
    числу слов документа(tf_matrix)."""
    return [[w / sum(d) for w in d] for d in count_matrix]


def test_task2():
    """Функция для тестирования функции tf_transform"""
    print("-----Тест для функции tf_transform-----", end="\n\n")
    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    ]
    tf_matrix = tf_transform(count_matrix)
    print(tf_matrix)
    print("-" * 100, end="\n\n")


# Задание #3: inverse document-frequency
# Реализуйте функцию idf_transform
def idf_transform(count_matrix: List[List[int]]) -> List[float]:
    """По матрице встречаймости слов в документах корпуса(count_matrix)
    возвращает матрицу инверсий частот, с которой некоторое слово
    встречается в документах коллекции(idf_matrix)."""
    word_frequency = [0] * len(count_matrix[0])
    for d in count_matrix:
        word_frequency = [x + bool(y) for x, y in zip(word_frequency, d)]
    return [log((len(count_matrix) + 1) / (w + 1)) + 1 for w in word_frequency]


def test_task3():
    """Функция для тестирования функции idf_transform"""
    print("-----Тест для функции idf_transform-----", end="\n\n")
    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    ]
    idf_matrix = idf_transform(count_matrix)
    print(idf_matrix)
    print("-" * 100, end="\n\n")


# Задание #4: tf-idf transformer
# Реализуйте класс TfidfTransformer, имеющий метод fit_transform
class TfidfTransformer:
    """Класс для вычисления tf-idf."""

    def tf_transform(count_matrix: List[List[int]]) -> List[List[float]]:
        """По матрице встречаймости слов в документах корпуса(count_matrix)
        возвращает матрицу отношений числа вхождений некоторого слова к общему
        числу слов документа(tf_matrix)."""
        return [[w / sum(d) for w in d] for d in count_matrix]

    def idf_transform(count_matrix: List[List[int]]) -> List[float]:
        """По матрице встречаймости слов в документах корпуса(count_matrix)
        возвращает матрицу инверсий частот, с которой некоторое слово
        встречается в документах коллекции(idf_matrix)."""
        word_frequency = [0] * len(count_matrix[0])
        for d in count_matrix:
            word_frequency = [x + bool(y) for x, y in zip(word_frequency, d)]
        return [
            log((len(count_matrix) + 1) / (w + 1)) + 1 for w in word_frequency
        ]

    def fit_transform(
        self, count_matrix: List[List[int]]
    ) -> List[List[float]]:
        """По матрице встречаймости слов в документах корпуса(count_matrix)
        возвращает матрицу статистических мер tf-idf для слов в документах
        корпуса(tfidf_matrix)."""
        tf_matrix = tf_transform(count_matrix)
        idf_matrix = idf_transform(count_matrix)
        return [
            [tf * idf for (tf, idf) in zip(tf_d, idf_matrix)]
            for tf_d in tf_matrix
        ]


def test_task4():
    """Функция для тестирования класса TfidfTransformer"""
    print("-----Тест для класса TfidfTransformer-----", end="\n\n")
    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    ]
    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(count_matrix)
    print(tfidf_matrix)
    print("-" * 100, end="\n\n")


# Задание #5: tf-idf vectorizer
# Реализуйте класс TfidfVectorizer, имеющий метод fit_transform
class TfidfVectorizer(CountVectorizer):
    """Класс для построения мешка слов(матрицы встречаймости слов в
    документах корпуса) на основе статистической меры tf-idf."""

    def fit_transform(self, corpus: List[str]) -> List[List[float]]:
        """Создаёт копию корпуса пользователя, для которого выполняет
        препроцессинг и токенизацию вычисляя словарь для всего корпуса и
        матрицу встречаймости слов в документах корпуса(tfidf_matrix)."""
        CountVectorizer.fit_transform(self, corpus)
        transformer = TfidfTransformer()
        return transformer.fit_transform(self.count_matrix)


def test_task5():
    """Функция для тестирования класса TfidfVectorizer"""
    print("-----Тест для класса TfidfVectorizer-----", end="\n\n")
    corpus = [
        "Crock Pot, Pasta55 Never boil& pasta? again",
        "Pasta Pomodoro Fresh 6ingredients6     Parmesan to taste!",
    ]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    # Проверяем, что corpus пользователя не изменился
    print("Корпус пользователя:\n{}".format(corpus), end="\n\n")
    print("Словарь:\n{}".format(vectorizer.get_feature_names()), end="\n\n")
    print("Tf-Idf матрица:\n{}".format(tfidf_matrix))
    print("-" * 100, end="\n\n")


if __name__ == "__main__":
    test_task1()
    test_task2()
    test_task3()
    test_task4()
    test_task5()
