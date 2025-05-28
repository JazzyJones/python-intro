# my_awesome_lib

Przykładowa biblioteka programistyczna w Pythonie, zawierająca narzędzia do przetwarzania danych, operacji matematycznych oraz pracy z tekstem.

---

## 📦 Opis

`my_awesome_lib` to pakiet stworzony w celach edukacyjnych. Pozwala na:
- Usuwanie duplikatów i spłaszczanie list
- Proste operacje matematyczne (silnia, sprawdzanie liczby pierwszej)
- Operacje na tekstach (zliczanie słów, odwracanie tekstu)

---

## 🔧 Instalacja

Aby zainstalować bibliotekę lokalnie, użyj polecenia:

pip install -e .

---

## 🚀 Przykłady użycia

from my_awesome_lib.data_utils import remove_duplicates, flatten
from my_awesome_lib.math_tools import factorial, is_prime
from my_awesome_lib.text_processing import count_words, reverse_text

print(remove_duplicates()) # 
print(flatten([, [3, # [1, 2, 3,t(factorial(5)) # 120
print(is_prime(7)) # True

print(count_words("Ala ma kota")) # 3
print(reverse_text("Python")) # nohtyP

---

## 🧪 Testy

Aby uruchomić testy jednostkowe:

python -m unittest discover tests


---

## 📁 Struktura projektu

zadanie_3/
│
├── my_awesome_lib/
│ ├── init.py
│ ├── data_utils.py
│ ├── math_tools.py
│ └── text_processing.py
│
├── tests/
│ ├── test_data_utils.py
│ ├── test_math_tools.py
│ └── test_text_processing.py
│
├── README.md
├── setup.py
└── .gitignore


---

## 👤 Autor

Sławomir Marczyk  
Wersja: 0.1  
Licencja: MIT

---

## 📄 Licencja

Projekt udostępniany na licencji MIT.

---

## 🛠️ Wkład

Chcesz się przyczynić? Zapraszamy do zgłaszania issue i pull requestów na GitHubie.

---

## ℹ️ Informacje dodatkowe

Projekt powstał w ramach laboratorium z programowania zaawansowanego w Pythonie (lab 3).
