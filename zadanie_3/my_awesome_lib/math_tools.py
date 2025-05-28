def factorial(n):
    """
    Zwraca silnię liczby n.
    :param n: liczba całkowita >= 0
    :return: silnia n
    :raises ValueError: dla n < 0
    """
    if n < 0:
        raise ValueError("Liczba musi być nieujemna")
    return 1 if n == 0 else n * factorial(n - 1)

def is_prime(n):
    """
    Sprawdza, czy liczba n jest pierwsza.
    :param n: liczba całkowita
    :return: True jeśli pierwsza, False w przeciwnym razie
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
