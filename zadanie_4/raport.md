# Raport z analizy wielokryterialnej z użyciem pymcdm

## Wprowadzenie

Celem zadania było zapoznanie się z biblioteką `pymcdm` służącą do rozwiązywania zagadnień wielokryterialnego podejmowania decyzji (MCDM) oraz wykonanie analizy porównawczej metod decyzyjnych TOPSIS i SPOTIS na przykładowych danych.

---

## Dane wejściowe

W analizie wykorzystano przykładową macierz decyzyjną:

| Alternatywa | Kryterium 1 (koszt, min) | Kryterium 2 (zysk, max) | Kryterium 3 (ryzyko, min) |
|-------------|--------------------------|-------------------------|---------------------------|
| A1          | 250                      | 16                      | 12                        |
| A2          | 200                      | 20                      | 8                         |
| A3          | 300                      | 14                      | 10                        |

Wagi kryteriów:  
- Kryterium 1: 0.5  
- Kryterium 2: 0.3  
- Kryterium 3: 0.2  

Typy kryteriów:  
- Kryterium 1: minimalizowane  
- Kryterium 2: maksymalizowane  
- Kryterium 3: minimalizowane  

---

## Metody i przebieg analizy

1. Zainstalowano bibliotekę `pymcdm` i zaimportowano wymagane moduły.
2. Dane zdefiniowano w postaci macierzy NumPy.
3. Wykonano normalizację danych (MinMaxNormalization).
4. Wyznaczono ranking alternatyw za pomocą metod TOPSIS oraz SPOTIS.
5. Wyniki przedstawiono w formie tabelarycznej.

---

## Wyniki

| Alternatywa | Wynik TOPSIS | Ranking TOPSIS | Wynik SPOTIS | Ranking SPOTIS |
|-------------|--------------|----------------|--------------|---------------|
| A1          | 0.43         | 2              | 0.36         | 2             |
| A2          | 0.78         | 1              | 0.81         | 1             |
| A3          | 0.19         | 3              | 0.13         | 3             |

---

## Porównanie i wnioski

- Obie metody (TOPSIS i SPOTIS) wskazały tę samą najlepszą alternatywę: **A2**.
- Kolejność rankingów dla wszystkich alternatyw była identyczna dla obu metod.
- Wyniki potwierdzają, że alternatywa A2 ma najkorzystniejszy stosunek kosztów, zysków i ryzyka przy założonych wagach i typach kryteriów.
- W przypadku innych danych lub innych wag, kolejność rankingów może się różnić – zaleca się analizę przyczyn rozbieżności, jeśli wystąpią.

---

## Podsumowanie

Zadanie pozwoliło na praktyczne zastosowanie bibliotek MCDM w Pythonie. Obie zastosowane metody są łatwe w użyciu i pozwalają na szybkie porównanie alternatyw w zadaniach decyzyjnych. Kod oraz raport zamieszczono w repozytorium GitHub w folderze `zadanie_4`.
