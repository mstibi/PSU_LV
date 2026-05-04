Zadatak 1
Skripta 5.1. učitava skup podataka koji se nalazi u csv datoteci occupancy_processed.csv. Ova datoteka sadrži podatke koji su prikupljeni u 
prostoriji veličine 6m x 4.6m tijekom 4 dana [1]. Zbog jednostavnosti skup sadrži samo dva atributa:
 mjerenja dobivena sa senzora temperature i mjerenja sa senzora CO2. 
Izlazna (ciljna) veličina je zauzetost prostorije (0 – prazna prostorija, 1 – u prostoriji se nalazi barem jedna osoba). 
Cilj je izgraditi klasifikator koji će na temelju trenutnih mjerenja dobivenih sa senzora temperature i sa senzora CO2 procijeniti zauzetost prostorije.

a) Pokrenite skriptu i pogledajte dobiveni dijagram raspršenja. Što primjećujete?

Na nekim dijelovima, tipa do otprilike pola grafa (po x osi), postoji jasna separacija između klasa, i u slučajevima di je prostorija zauzeta je C02 vidljivo veći, 
ali tada postoji dio na dijagramu, od 25.25 - 25.75, gdje se klase malo više preklapaju, i što je veća temperatura, to je veći udio C02 indikator da je prostorija slobodna

b) Koliko podatkovnih primjera sadrži učitani skup podataka?

10129 primjera.

c) Kakva je razdioba podatkovnih primjera po klasama?

Klasa 0 (prazna prostorija) ima 8228 primjera
Klasa 1 (zauzeta prostorija) ima 1901 primjer
Većina podataka pripada klasi 0 (oko 81%), dok je klasa 1 (oko 19%)

Zadatak 2
Izgradite i evaluirajte algoritam K najbližih susjeda. Slijedite ovaj redoslijed:
a) Podijelite podatke na skup za učenje i skup za testiranje (omjer 80%-20%) pomoću funkcije train_test_split. Koristite opciju stratify=y.
b) Pomoću StandardScaler skalirajte ulazne veličine.
c) Pomoću klase KNeighborsClassifier izgradite algoritam K najbližih susjeda.
d) Evaluirajte izgrađeni klasifikator na testnom skupu podataka:
a. prikažite matricu zabune



import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, precision_score, recall_score

# 1. Učitavanje podataka

data = pd.read_csv("occupancy_processed.csv")

X = data[['S3_Temp', 'S5_CO2']]
y = data['Room_Occupancy_Count']


# 2. Podjela skupa

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# 3. Skaliranje podataka

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# 4. KNN klasifikator

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train_scaled, y_train)

# 5. Predikcija

y_pred = knn.predict(X_test_scaled)

# 6. Evaluacija

# Matrica zabune
cm = confusion_matrix(y_test, y_pred)
print("Matrica zabune:")
print(cm)

# Točnost
accuracy = accuracy_score(y_test, y_pred)
print("\nTočnost:", accuracy)

# Preciznost i odziv
preciznost = precision_score(y_test, y_pred)
print("\nPreciznost:", preciznost)

odziv = recall_score(y_test, y_pred)
print("\nOdziv: ", odziv)


Matrica zabune:
[[1584   62]
 [  30  350]]

b. izračunajte točnost klasifikacije

Točnost: 0.9545903257650543

c. izračunajte preciznost i odziv po klasama
klasa   preciznost    odziv
0       0.96          0.97
1       0.92          0.88 

e) Što se događa s rezultatima ako se koristi veći odnosno manji broj susjeda?
Sa 2 neighbora: 

Točnost: 0.9521224086870681

klasa   preciznost   odziv
0       0.98         0.97 
1       0.83         0.87

Sa 3 neighbora: 

Točnost: 0.9565646594274433

klasa   preciznost   odziv
0       0.96         0.97
1       0.94         0.89

Točnost je ostala slična, malo je lošija. Sa 3 i 5 neighbora, rezultati su gotovo pa isti, čak su preciznost i odziv za klasu 1 bolji sa 3 neighbora, kao i točnost, ali zato s 2 neighbora
su rezultati tu malo drugačiji, točnost je za 0.5% lošija od 3 neighbora, preciznost za klasu 0 je bolja i odziv je jednak, dok za klasu 1 je velika razlika u preciznosti kod 2 neighbora, za 11%.

f) Što se događa s rezultatima ako ne koristite skaliranje ulaznih veličina?

Matrica zabune:
[[1569   77]
 [  60  320]]
klasa    preciznost  odziv
 0       0.95        0.96
 1       0.84        0.82


(Prikazuju se i uspoređuju podaci sa 5 neighbora)
Uglavnom, bilo je više False Positive i False Negative rezultata, što naravno narušava svaku metriku.

Zadatak 3
Umjesto algoritma K najbližih susjeda koristite stablo odlučivanja te ponovite korake a) do d) iz prethodnog zadatka.

a) Vizualizirajte dobiveno stablo odlučivanja.
b) Što se događa s rezultatima ako mijenjate parametar max-depth stabla odlučivanja?

max depth 5:

Matrica zabune:
[[1579   67]
 [  52  328]]

Točnost: 0.941263573543929

Preciznost: 0.830379746835443

Odziv:  0.8631578947368421

max depth 3:

Matrica zabune:
[[1558   88]
 [  83  297]]

Točnost: 0.9155972359328727

Preciznost: 0.7714285714285715

Odziv:  0.781578947368421

max depth 10: 

Matrica zabune:
[[1597   49]
 [  36  344]]

Točnost: 0.9580454096742349

Preciznost: 0.8753180661577609

Odziv:  0.9052631578947369

Kako povećavamo max depth, to imamo više čvorova i sve metrike su bolje

c) Što se događa s rezultatima ako ne koristite skaliranje ulaznih veličina?

Rezultati se prikazuju za max depth 5;

Matrica zabune:
[[1579   67]
 [  52  328]]

Točnost: 0.941263573543929

Preciznost: 0.830379746835443

Odziv:  0.8631578947368421

Kod stabla odlučivanja, rezultati se uopće ne mijenjaju kad se makne skaliranje zato što stablo odlučivanja NE koristi udaljenosti, nego usporedbe.

Zadatak 4
Po uzoru na prethodne zadatke izgradite model logističke regresije. Što primjećujete kod vrednovanja ovog modela? Što je uzrok dobivenim rezultatima?


import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, precision_score, recall_score

import matplotlib.pyplot as plt

data = pd.read_csv("occupancy_processed.csv")

X = data[['S3_Temp', 'S5_CO2']]
y = data['Room_Occupancy_Count']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression() 
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

cm = confusion_matrix(y_test, y_pred)
print("Matrica zabune:")
print(cm)

accuracy = accuracy_score(y_test, y_pred)
print("\nTočnost:", accuracy)

rezultati = classification_report(y_test, y_pred)
print("\nRezultati:", rezultati)



Točnost: 0.9007897334649556

klasa   precision recall
0       0.92      0.96      
1       0.80      0.63           

U usporedbi sa drugim modelima, ovaj zadatak klasu 0 jako dobro predicta, ali zato klasu 1 užasno, preciznost je 80%, a odziv 0.63, što je znatno manje nego klasu 0.
To se događa jer podaci nisu baš odvojivi, znači da da se preklapaju međusobno, blizu su jedni drugih, itd; a logistička regresija je linearan model.