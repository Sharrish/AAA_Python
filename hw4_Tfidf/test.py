from hw4_Tfidf import (
    CountVectorizer,
    tf_transform,
    idf_transform,
    TfidfTransformer,
    TfidfVectorizer,
)


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
