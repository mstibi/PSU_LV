import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


# MNIST podatkovni skup
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()


# TODO: prikazi nekoliko slika iz train skupa
plt.figure(figsize=(10, 4))

for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_train[i], cmap="gray")
    plt.title(f"Oznaka: {y_train[i]}")
    plt.axis("off")

plt.tight_layout()
plt.show()


# Skaliranje vrijednosti piksela na raspon [0,1]
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

# Slike 28x28 piksela se predstavljaju vektorom od 784 elementa
x_train_s = x_train_s.reshape(60000, 784)
x_test_s = x_test_s.reshape(10000, 784)

# Kodiraj labele (0, 1, ... 9) one hot encoding-om
y_train_s = keras.utils.to_categorical(y_train, 10)
y_test_s = keras.utils.to_categorical(y_test, 10)


# TODO: kreiraj mrezu pomocu keras.Sequential(); prikazi njenu strukturu pomocu .summary()
model = keras.Sequential([
    keras.Input(shape=(784,)),

    layers.Dense(512, activation="relu"),
    layers.Dense(256, activation="relu"),

    layers.Dense(10, activation="softmax")
])

model.summary()


# TODO: definiraj karakteristike procesa ucenja pomocu .compile()
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)


# TODO: provedi treniranje mreze pomocu .fit()
history = model.fit(
    x_train_s,
    y_train_s,
    epochs=10,
    batch_size=128,
    validation_split=0.1
)


# TODO: Izracunajte tocnost mreze na skupu podataka za ucenje i skupu podataka za testiranje
train_loss, train_acc = model.evaluate(x_train_s, y_train_s, verbose=0)
test_loss, test_acc = model.evaluate(x_test_s, y_test_s, verbose=0)

print("Točnost na skupu za učenje:", train_acc)
print("Točnost na testnom skupu:", test_acc)


# Predikcije za train i test skup
y_train_pred_prob = model.predict(x_train_s)
y_test_pred_prob = model.predict(x_test_s)

y_train_pred = np.argmax(y_train_pred_prob, axis=1)
y_test_pred = np.argmax(y_test_pred_prob, axis=1)


# TODO: Prikazite matricu zabune na skupu podataka za ucenje
cm_train = confusion_matrix(y_train, y_train_pred)

disp_train = ConfusionMatrixDisplay(
    confusion_matrix=cm_train,
    display_labels=np.arange(10)
)

disp_train.plot(cmap="Blues")
plt.title("Matrica zabune - skup za učenje")
plt.show()


# TODO: Prikazite matricu zabune na skupu podataka za testiranje
cm_test = confusion_matrix(y_test, y_test_pred)

disp_test = ConfusionMatrixDisplay(
    confusion_matrix=cm_test,
    display_labels=np.arange(10)
)

disp_test.plot(cmap="Blues")
plt.title("Matrica zabune - testni skup")
plt.show()


# TODO: Prikazi nekoliko primjera iz testnog skupa podataka koje je izgrađena mreza pogresno klasificirala
wrong_indices = np.where(y_test != y_test_pred)[0]

# Nasumično odaberi nekoliko pogrešno klasificiranih primjera
random_wrong_indices = np.random.choice(wrong_indices, size=10, replace=False)

plt.figure(figsize=(12, 5))

for i, index in enumerate(random_wrong_indices):
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_test[index], cmap="gray")
    plt.title(f"Stvarno: {y_test[index]}, Procjena: {y_test_pred[index]}")
    plt.axis("off")

plt.tight_layout()
plt.show()

#Dobiveni rezultati pokazuju visoku točnost mreže. Matrica zabune ima najveće vrijednosti na glavnoj dijagonali, što znači da je većina znamenki ispravno prepoznata.
#Pogreške su uglavnom kod vizualno sličnih znamenki, iako se da pronaći izuzetak. Ako je testna točnost malo manja od točnosti na skupu za učenje, mreža dobro generalizira.