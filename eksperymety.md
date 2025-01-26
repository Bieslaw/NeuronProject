## Podstawowy model:
* średnia z dni jako wejście
* ReLU
* jedna warstwa 256 neuronów
* MSE, crossentropy - loss
* kodowanie dnia roku jako liczba, miesiąc jako klasa
* lr=0.0001, 400 epok, batch_size 512, dla wiatru lr=0.001, 200 epok

### 1. **Kodowanie danych**  
- **Trygonometryczne:** kierunek wiatru i czas (godzina/dzień roku) kodowane jako `sin/cos`.  
- **Liniowe:** surowe wartości liczbowe.  
- **Cel:** Sprawdź, która metoda lepiej uchwyci cykliczność.

---

### 2. **Miary błędu**  
- **Temperatura:** MSE vs MAE.  
- **Wiatr:** Binary Cross-Entropy vs Focal Loss.  
- **Cel:** Wybierz metrykę lepiej pasującą do celów (MAE ≤2°C, Focal Loss dla rzadkich zdarzeń).

---

### 3. **Architektury sieci**  
0. **Model bazowy** 1 warstwa 256 neuornów
1. **Model A:** 3 warstwy (256 → 256 → 256).  
2. **Model B:** Jak A, ale z 50% usuniętych połączeń.  
1. **Model C:** 3 warstwy (256 → 128 → 64).  
- **Cel:** Porównaj wpływ struktury sieci na wyniki.

---

### 4. **Funkcje aktywacji**  
- **Ukryte:** ReLU vs Sigmoid.  
- **Wyjście:** Linear (temperatura), Sigmoid (wiatr).  

---

### 5. **Agregacja danych**  
- **Surowe dane:** 72 godziny.  
- **Agregacja:** 3 średnie dzienne.  
- **Cel:** Sprawdź, czy agregacja redukuje szum.

---

### 6. **Predykcja z dniem pośrednim**  
1. Trenuj Model A: dni *t-3, t-2, t-1* → dzień *t*.  
2. Trenuj Model B: dni *t-2, t-1* + **predykcja A** → dzień *t+1*.  
- **Wymagane:** Dwa osobne modele.