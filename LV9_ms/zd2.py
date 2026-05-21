import json
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow.keras.preprocessing import image


MODEL_PATH = "best_gtsrb_model.keras"
CLASS_NAMES_PATH = "class_names.json"
IMAGE_PATH = "moj_znak.jpg"

IMG_SIZE = (48, 48)


model = tf.keras.models.load_model(MODEL_PATH)

with open(CLASS_NAMES_PATH, "r", encoding="utf-8") as f:
    class_names = json.load(f)


img = image.load_img(
    IMAGE_PATH,
    target_size=IMG_SIZE
)

img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)


predictions = model.predict(img_array)

predicted_index = np.argmax(predictions[0])
confidence = predictions[0][predicted_index]

predicted_class = class_names[predicted_index]

print("Predviđena klasa:", predicted_class)
print("Pouzdanost:", round(confidence * 100, 2), "%")


plt.imshow(img)
plt.title(f"Predikcija: {predicted_class} ({confidence * 100:.2f}%)")
plt.axis("off")
plt.show()