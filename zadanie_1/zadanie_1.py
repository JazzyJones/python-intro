# zadanie_1.py

# Tworzenie dwóch list
list_a = [1, 2, 3]
list_b = ['a', 'b', 'c']

# Łączenie list funkcją zip()
zipped = zip(list_a, list_b)
print("Złączone listy:", list(zipped))  # Dokumentacja: https://docs.python.org/3/library/functions.html#zip

# Wykorzystanie funkcji z modułu math
import math
num = 16
print("Pierwiastek kwadratowy z", num, "wynosi:", math.sqrt(num))  # Dokumentacja: https://docs.python.org/3/library/math.html

# Obsługa wyjątku try-except
try:
    result = num / 0
except ZeroDivisionError as e:
    print("Błąd:", e)  # Dokumentacja: https://docs.python.org/3/library/exceptions.html#ZeroDivisionError
