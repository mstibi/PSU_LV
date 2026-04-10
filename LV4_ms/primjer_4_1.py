import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

# funkcije


def non_func(x):
    return 1.6345 - 0.6235*np.cos(0.6067*x) - 1.3501*np.sin(0.6067*x) \
        - 1.1622*np.cos(2*x*0.6067) - 0.9443*np.sin(2*x*0.6067)


def add_noise(y):
    np.random.seed(14)
    varNoise = np.max(y) - np.min(y)
    return y + 0.1*varNoise*np.random.normal(0, 1, len(y))


# generiranje podataka
x = np.linspace(1, 10, 100)
y_true = non_func(x)
y_measured = add_noise(y_true)

x = x[:, np.newaxis]
y_measured = y_measured[:, np.newaxis]

# podjela na train/test
np.random.seed(12)
indeksi = np.random.permutation(len(x))
indeksi_train = indeksi[:int(0.7*len(x))]
indeksi_test = indeksi[int(0.7*len(x)):]

degrees = [2, 6, 15]

MSEtrain = []
MSEtest = []

plt.figure()

for d in degrees:
    poly = PolynomialFeatures(degree=d)
    x_poly = poly.fit_transform(x)

    xtrain = x_poly[indeksi_train]
    xtest = x_poly[indeksi_test]

    ytrain = y_measured[indeksi_train]
    ytest = y_measured[indeksi_test]

    model = lm.LinearRegression()
    model.fit(xtrain, ytrain)

    # predikcije
    ytrain_p = model.predict(xtrain)
    ytest_p = model.predict(xtest)

    # MSE
    MSEtrain.append(mean_squared_error(ytrain, ytrain_p))
    MSEtest.append(mean_squared_error(ytest, ytest_p))

    # crtanje modela
    plt.plot(x, model.predict(x_poly), label=f'degree={d}')

# crtanje stvarne funkcije
plt.plot(x, y_true, 'k--', label='stvarna funkcija')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Usporedba modela')
plt.show()

print("MSEtrain:", MSEtrain)
print("MSEtest:", MSEtest)
