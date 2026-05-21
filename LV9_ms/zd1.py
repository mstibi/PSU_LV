import os
import json
import datetime
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Rescaling,
    Conv2D,
    MaxPooling2D,
    Flatten,
    Dense,
    Dropout
)
from tensorflow.keras.callbacks import ModelCheckpoint, TensorBoard
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report


TRAIN_DIR = "gtsrb/Train"
TEST_DIR = "gtsrb/Test"

IMG_SIZE = (48, 48)
BATCH_SIZE = 32
SEED = 123
EPOCHS = 10


train_ds = image_dataset_from_directory(
    directory=TRAIN_DIR,
    labels="inferred",
    label_mode="categorical",
    batch_size=BATCH_SIZE,
    image_size=IMG_SIZE,
    validation_split=0.2,
    subset="training",
    seed=SEED
)

validation_ds = image_dataset_from_directory(
    directory=TRAIN_DIR,
    labels="inferred",
    label_mode="categorical",
    batch_size=BATCH_SIZE,
    image_size=IMG_SIZE,
    validation_split=0.2,
    subset="validation",
    seed=SEED
)

test_ds = image_dataset_from_directory(
    directory=TEST_DIR,
    labels="inferred",
    label_mode="categorical",
    batch_size=BATCH_SIZE,
    image_size=IMG_SIZE,
    shuffle=False
)

class_names = train_ds.class_names
num_classes = len(class_names)

print("Broj klasa:", num_classes)
print("Klase:", class_names)

with open("class_names.json", "w", encoding="utf-8") as f:
    json.dump(class_names, f, indent=4)


AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
validation_ds = validation_ds.cache().prefetch(buffer_size=AUTOTUNE)
test_ds = test_ds.cache().prefetch(buffer_size=AUTOTUNE)


model = Sequential([
    Rescaling(1.0 / 255, input_shape=(48, 48, 3)),

    # Blok 1, x = 32
    Conv2D(32, (3, 3), strides=1, padding="same", activation="relu"),
    Conv2D(32, (3, 3), strides=1, padding="valid", activation="relu"),
    MaxPooling2D((2, 2)),
    Dropout(0.2),

    # Blok 2, x = 64
    Conv2D(64, (3, 3), strides=1, padding="same", activation="relu"),
    Conv2D(64, (3, 3), strides=1, padding="valid", activation="relu"),
    MaxPooling2D((2, 2)),
    Dropout(0.2),

    # Blok 3, x = 128
    Conv2D(128, (3, 3), strides=1, padding="same", activation="relu"),
    Conv2D(128, (3, 3), strides=1, padding="valid", activation="relu"),
    MaxPooling2D((2, 2)),
    Dropout(0.2),

    Flatten(),

    Dense(512, activation="relu"),
    Dropout(0.5),

    Dense(43, activation="softmax")
])

model.summary()



model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)


checkpoint = ModelCheckpoint(
    filepath="best_gtsrb_model.keras",
    monitor="val_accuracy",
    save_best_only=True,
    mode="max",
    verbose=1
)

log_dir = os.path.join(
    "logs",
    "fit",
    datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
)

tensorboard = TensorBoard(
    log_dir=log_dir,
    histogram_freq=1
)


history = model.fit(
    train_ds,
    validation_data=validation_ds,
    epochs=EPOCHS,
    callbacks=[checkpoint, tensorboard]
)


best_model = tf.keras.models.load_model("best_gtsrb_model.keras")

test_loss, test_accuracy = best_model.evaluate(test_ds)

print("\nTočnost na testnom skupu:")
print(test_accuracy)


y_true = []
y_pred = []

for images, labels in test_ds:
    predictions = best_model.predict(images, verbose=0)

    true_classes = np.argmax(labels.numpy(), axis=1)
    predicted_classes = np.argmax(predictions, axis=1)

    y_true.extend(true_classes)
    y_pred.extend(predicted_classes)

y_true = np.array(y_true)
y_pred = np.array(y_pred)

cm = confusion_matrix(y_true, y_pred)

fig, ax = plt.subplots(figsize=(14, 14))

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=class_names
)

disp.plot(
    ax=ax,
    cmap=plt.cm.Blues,
    xticks_rotation=90,
    colorbar=True
)

plt.title("Matrica zabune - GTSRB")
plt.tight_layout()
plt.show()

print("\nKlasifikacijski izvještaj:")
print(classification_report(y_true, y_pred, target_names=class_names))