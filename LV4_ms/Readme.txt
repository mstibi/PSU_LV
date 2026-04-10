Zadatak 1:

# generiranje podataka
np.random.seed(0)
x = np.linspace(1, 10, 100)
y_true = np.sin(x)  # stvarna funkcija
y = y_true + 0.3*np.random.randn(len(x))  # dodan šum

# reshape
X = x.reshape(-1, 1)

# podjela
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2)

# stupnjevi polinoma
degrees = [2, 6, 15]

MSEtrain = []
MSEtest = []

plt.figure(figsize=(10, 6))

# petlja kroz modele
for d in degrees:

    poly = PolynomialFeatures(degree=d)

    Xtrain_poly = poly.fit_transform(Xtrain)
    Xtest_poly = poly.transform(Xtest)

    model = LinearRegression()
    model.fit(Xtrain_poly, ytrain)

    # predikcije
    ytrain_pred = model.predict(Xtrain_poly)
    ytest_pred = model.predict(Xtest_poly)

    # spremanje MSE
    MSEtrain.append(mean_squared_error(ytrain, ytrain_pred))
    MSEtest.append(mean_squared_error(ytest, ytest_pred))

    # crtanje funkcije
    x_plot = np.linspace(1, 10, 200).reshape(-1, 1)
    y_plot = model.predict(poly.transform(x_plot))

    plt.plot(x_plot, y_plot, label=f"degree={d}")

# stvarna funkcija
plt.plot(x, y_true, 'k--', label="stvarna funkcija")

# podaci
plt.scatter(Xtrain, ytrain, color='blue', s=10, label="train")
plt.scatter(Xtest, ytest, color='red', s=10, label="test")

Zadatak 2.

primjer 4.1. - model je linearna regresija, on je pravac, ima underfitting
primjer 4.2. - model nije linearan, može koristiti složenije funkcije, koristi PolynomialFeatures i ima mogućnost transformiranja ulaza, te se vidi overfitting.

Polinomni model iz drugog primjera bolje aproksimira stvarnu funkciju jer uvodi nelinearnost, ali zbog visokog stupnja polinoma (15) model se previše prilagođava podacima za učenje, što može dovesti do problema s novim podacima - overfittinga.

Zadatak 3.

Povećanjem stupnja polinoma model postaje fleksibilniji, ali potrebno je znati gdje "stati". Za mali stupanj dolazi do underfittinga, dok za veliki stupanj dolazi do overfittinga. Optimalan model postiže kompromis između ta dva efekta. Također, veći broj uzoraka za učenje smanjuje overfitting i poboljšava generalizaciju modela.

U ovom konkretnom primjeru, stupanj 2 je veliki promašaj, dolazi do ogromnog underfittinga i ne prati podatke gotovo uopće, dok se za stupnjeve 6 i 15 od oka ne može odlučiti koji je bliži stvarnoj funkciji, npr. stupanj 6 u nekim djelovima underfitta, dok stupanj 15 overfitta, ali su tu negdje.

Zadatak 4. 

1. Koliko mjerenja (automobila) je dostupno u datasetu?
	U datasetu se nalazi 6699 automobila.

2. Kakav je tip pojedinog stupca u dataframeu?

df.info():year = int
selling_price = float
km_driven = int
mileage = float
engine = int
max_power = float
seats = int
name = object
fuel = object
seller_type = object
transmission = object
owner = object

3. Koji automobil ima najveću cijenu, a koji najmanju?

Najveća cijena:
godina: 2020
cijena: 15.789592
gorivo: Diesel
mjenjač: Automatic

Najmanja cijena:

godina: 1997
cijena: 10.308919
gorivo: Petrol
mjenjač: Manual

4. Koliko automobila je proizvedeno 2012. godine?

575 

5. Koji automobil je prešao najviše kilometara, a koji najmanje?

Najviše kilometara:
577414 km
godina: 2010
gorivo: Petrol

Najmanje kilometara:
1 km
godina: 2011
gorivo: CNG

6. Koliko najčešće automobili imaju sjedala?

5

7. Kolika je prosječna prijeđena kilometraža za automobile s dizel motorom, a koliko za automobile s benzinskim motorom?
Diesel: 88039.97 km
Petrol: 54101.88 km

Zadatak 5.

Model: 

import numpy as np
import pandas as pd
import sklearn.linear_model as lm

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error, max_error

df = pd.read_csv('cars_processed.csv')

df = df.drop(['name'], axis=1)

df_num = df.select_dtypes(include=np.number)

X = df_num.drop('selling_price', axis=1)
y = df_num['selling_price']

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
Xtrain = scaler.fit_transform(Xtrain)
Xtest = scaler.transform(Xtest)

model = lm.LinearRegression()
model.fit(Xtrain, ytrain)

ytrain_pred = model.predict(Xtrain)
ytest_pred = model.predict(Xtest)

print("TRAIN:")
print("MAE:", mean_absolute_error(ytrain, ytrain_pred))
print("MSE:", mean_squared_error(ytrain, ytrain_pred))
print("R2:", r2_score(ytrain, ytrain_pred))
print("MAX ERROR:", max_error(ytrain, ytrain_pred))

print("\nTEST:")
print("MAE:", mean_absolute_error(ytest, ytest_pred))
print("MSE:", mean_squared_error(ytest, ytest_pred))
print("R2:", r2_score(ytest, ytest_pred))
print("MAX ERROR:", max_error(ytest, ytest_pred))

Za izgradnju modela korištene su samo numeričke varijable - znači stupac name je izbačen. Podaci su podijeljeni na skup za učenje i testiranje u omjeru 80 : 20. Ulazne varijable su skalirane sa StandardScaler metodom. Na tim podacima izgrađen je linearni regresijski model. Model je evaluiran pomoću metrika MAE, MSE, R² i maksimalne pogreške.

6. Što se događa s pogreškom na testnom skupu kada mijenjate broj ulaznih veličina?

Ako koristimo više podataka o autu, model bolje uči, ali previše podataka može učiniti da se model prilagodi samo trening setu i loše predviđa nove primjere. Premalo podataka znači da model ne uči dovoljno. Treba naći zlatnu sredinu.


Zadatak 6.Dodajte u model iz prethodnog zadatka i kategoričke varijable. Pri tome koristite pandas funkciju pd.get_dummies za one hot kodiranje kategoričkih veličina. Jesu li se značajno poboljšali rezultati?

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


df = pd.read_csv('cars_processed.csv')
df = df.drop(['name'], axis=1)

categorical_cols = ['fuel', 'seller_type', 'transmission', 'owner']
df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

X = df_encoded.drop('selling_price', axis=1)
y = df_encoded['selling_price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

numerical_cols = ['year', 'km_driven',
                  'engine', 'mileage', 'max_power', 'seats']
scaler = MinMaxScaler()
X_train[numerical_cols] = scaler.fit_transform(X_train[numerical_cols])
X_test[numerical_cols] = scaler.transform(X_test[numerical_cols])

model = LinearRegression()
model.fit(X_train, y_train)

y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

print("MSE na trening skupu:", mean_squared_error(y_train, y_train_pred))
print("MSE na test skupu:", mean_squared_error(y_test, y_test_pred))

One-hot encoding pretvara kategorije u 0/1 stupce i model sada vidi više informacija, uključujući tip goriva, tip prodavača itd.
Obično rezultati blago poboljšavaju MSE, posebno na test skupu, jer model sada može razlikovati cijene automobila po kategorijama.
