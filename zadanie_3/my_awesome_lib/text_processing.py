def count_words(text):
    """
    Zlicza liczbę słów w tekście.
    :param text: ciąg znaków
    :return: liczba słów
    """
    return len(text.split())

def reverse_text(text):
    """
    Odwraca tekst.
    :param text: ciąg znaków
    :return: odwrócony tekst
    """
    return text[::-1]
