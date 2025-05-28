# Raport – Web scraping w Pythonie

## 1. BeautifulSoup
- **Przeznaczenie**: Parsowanie i analiza kodu HTML/XML.
- **Główne funkcje**: Łatwe wyszukiwanie elementów, filtrowanie, modyfikacja drzewa DOM.
- **Zalety**: Prosta składnia, duża społeczność, dobra dokumentacja.
- **Ograniczenia**: Sam nie pobiera stron – wymaga np. requests.
- **Dokumentacja**: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

## 2. Requests
- **Przeznaczenie**: Pobieranie zawartości stron www (HTTP).
- **Główne funkcje**: Obsługa GET/POST, sesje, autoryzacja, obsługa cookies.
- **Zalety**: Bardzo prosta składnia, obsługa wielu funkcji HTTP.
- **Ograniczenia**: Nie parsuje HTML – wymaga np. BeautifulSoup.
- **Dokumentacja**: https://requests.readthedocs.io/

## Podsumowanie
Obie biblioteki świetnie się uzupełniają – Requests pobiera dane, BeautifulSoup je przetwarza.
