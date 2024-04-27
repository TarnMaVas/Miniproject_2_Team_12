"""Function that places "диво" before the "flag" in given "sentence"""

def dyvo_insert(sentence : str, flag : str) -> str:
    """
    (str, str) -> str
    Places "диво" before the "flag" in given "sentence"
    If arguments are not string, the function should return None.

    >>> dyvo_insert("Кит кота по хвилях катав - кит у воді, кіт на киті.", 'ки')
    'Дивокит кота по хвилях катав - дивокит у воді, кіт на дивокиті.'

    """
    if isinstance(sentence, str) and isinstance(flag, str):
        flag = flag.lower()
        if sentence.startswith(flag):
            sentence = 'диво' + sentence
        replacement = f'диво{flag}'
        sentence = sentence.replace(' ' + flag, ' ' + replacement)
        sentence = sentence.replace(flag.capitalize(), replacement.capitalize())
        return sentence

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
