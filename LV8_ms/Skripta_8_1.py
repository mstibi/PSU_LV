from tensorflow import keras
from tensorflow.keras import layers, models, callbacks
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np
import matplotlib.pyplot as plt
import os

# MNIST podatkovni skup
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Priprema podataka za CNN: 28x28 slika + 1 kanal
x_train_s = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test_s = x_test.reshape(-1, 28, 28, 1) / 255.0

# One-hot encoding oznaka
y_train_s = to_categorical(y_train, num_classes=10)
y_test_s = to_categorical(y_test, num_classes=10)

# 1) Struktura konvolucijske neuronske mreže

model = models.Sequential()

model.add(layers.Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))

model.add(layers.Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))

model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.summary()

# 2) Compile modela

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# 3) Callbacks: TensorBoard + spremanje najboljeg modela

log_dir = "logs/mnist_cnn"
best_model_path = "best_mnist_cnn.keras"

tensorboard_callback = callbacks.TensorBoard(
    log_dir=log_dir,
    histogram_freq=1
)

checkpoint_callback = callbacks.ModelCheckpoint(
    filepath=best_model_path,
    monitor='val_accuracy',
    save_best_only=True,
    mode='max',
    verbose=1
)

# 4) Treniranje mreže
# 10% podataka za validaciju -> validation_split=0.1

history = model.fit(
    x_train_s,
    y_train_s,
    epochs=10,
    batch_size=128,
    validation_split=0.1,
    callbacks=[tensorboard_callback, checkpoint_callback]
)

# Provjera je li model spremljen
if os.path.exists(best_model_path):
    print("Najbolji model je spremljen na disk:", best_model_path)
else:
    print("Najbolji model NIJE spremljen.")

# 5) Učitavanje najboljeg modela

best_model = models.load_model(best_model_path)

# Točnost na skupu za učenje
train_loss, train_accuracy = best_model.evaluate(x_train_s, y_train_s, verbose=0)

# Točnost na skupu za testiranje
test_loss, test_accuracy = best_model.evaluate(x_test_s, y_test_s, verbose=0)

print("Točnost najboljeg modela na skupu za učenje:", train_accuracy)
print("Točnost najboljeg modela na skupu za testiranje:", test_accuracy)

# 6) Matrica zabune za skup za učenje

y_train_pred_prob = best_model.predict(x_train_s)
y_train_pred = np.argmax(y_train_pred_prob, axis=1)

cm_train = confusion_matrix(y_train, y_train_pred)

print("\nMatrica zabune - skup za učenje:")
print(cm_train)

plt.figure(figsize=(8, 6))
plt.imshow(cm_train, cmap='Blues')
plt.title("Matrica zabune - skup za učenje")
plt.xlabel("Predviđena klasa")
plt.ylabel("Stvarna klasa")
plt.colorbar()
plt.show()

# 7) Matrica zabune za skup za testiranje

y_test_pred_prob = best_model.predict(x_test_s)
y_test_pred = np.argmax(y_test_pred_prob, axis=1)

cm_test = confusion_matrix(y_test, y_test_pred)

print("\nMatrica zabune - skup za testiranje:")
print(cm_test)

plt.figure(figsize=(8, 6))
plt.imshow(cm_test, cmap='Blues')
plt.title("Matrica zabune - skup za testiranje")
plt.xlabel("Predviđena klasa")
plt.ylabel("Stvarna klasa")
plt.colorbar()
plt.show()

#Model postiže visoku točnost na skupu za učenje i skupu za testiranje, što pokazuje da je konvolucijska
# neuronska mreža dobro naučila prepoznavati znamenke iz MNIST skupa podataka. 
# Točnost na skupu za učenje je očekivano malo veća jer je model treniran na tim podacima.

#Matrice zabune pokazuju da se najveći broj vrijednosti nalazi na glavnoj dijagonali, 
#što znači da model većinu znamenki ispravno klasificira. 
#Pogreške se najčešće pojavljuju kod vizualno sličnih znamenki, npr. 3 i 5, 3 i 8 ili 7 i 1.