import re
from typing import List
from collections import Counter
from copy import deepcopy


class CountVectorizer:
    """Класс для построения мешка слов"""

    def __init__(self, lowercase: bool = True, clear: bool = True):
        self.lowercase = lowercase
        self.clear = clear
        self._vocabulary = {}
        self._count_matrix = []

    def _preprocess(self, X: List[str]):
        """Проводит препроцессинг корпуса - приведение всех экземпляров к
        нижнему регистру и удаление всех небуквенных символов,
        кроме пробелов"""
        if self.lowercase:  # приведение к нижнему регистру
            for i in range(len(X)):
                X[i] = X[i].lower()
        if self.clear:  # удаление всех небуквенных символов, кроме пробелов
            for i in range(len(X)):
                X[i] = re.sub(r'\s', ' ', X[i])  # whitespace characters -> ' '
                X[i] = re.sub(r' +', ' ', X[i])  # несколько пробелов в один
                # Оставляем только буквы и пробелы:
                X[i] = re.sub(r'[^A-Za-zА-Яа-я ]', '', X[i])

    def _tokeniser(self, X: List[str]):
        """Проводит токенизацию корпуса по всем whitespace символам"""
        # str.split() without an argument splits on whitespace:
        for i in range(len(X)):
            X[i] = X[i].split()

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """Создаёт копию корпуса пользователя, для которого выполняет
        препроцессинг и токенизацию вычисляя словарь для всего корпуса и
        мешок слов корпуса"""
        X = deepcopy(corpus)  # чтобы corpus пользователя не менялся
        self._preprocess(X)
        self._tokeniser(X)
        c = Counter()
        for x in X:
            c.update(x)
        self._vocabulary = c
        for x in X:
            c = Counter(x)
            one_hot_vector = [c[word] for word in self._vocabulary]
            self._count_matrix.append(one_hot_vector)
        return self._count_matrix

    def get_feature_names(self) -> List[str]:
        """Возвращает все слова, которые встречаются в корпусе"""
        return list(self._vocabulary.keys())


if __name__ == '__main__':
    corpus = [
        'Crock Pot, Pasta55 Never boil& pasta? again',
        'Pasta Pomodoro Fresh 6ingredients6     Parmesan to taste!'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    # Проверяем, что corpus пользователя не изменился
    print("Корпус пользователя:\n{}".format(corpus), end='\n\n')
    print("Словарь:\n{}".format(vectorizer.get_feature_names()), end='\n\n')
    print("Мешок слов:\n{}".format(count_matrix))
