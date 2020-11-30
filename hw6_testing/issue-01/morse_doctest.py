from morse import LETTER_TO_MORSE


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвие с таблицей азбуки Морзе.

    >>> encode('SOS')
    '... --- ...'
    >>> encode('SAIT')
    '... .- .. -'
    >>> encode('lowercase')
    Traceback (most recent call last):
    KeyError: 'l'
    >>> encode(777)
    Traceback (most recent call last):
    TypeError: 'int' object is not iterable
    >>> list(encode('S'*20)) # doctest: +ELLIPSIS
    ['.', '.', '.', ' ', ... ' ', '.', '.', '.']
    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)
