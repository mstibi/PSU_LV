import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.transform import resize
from skimage import color
from skimage.filters import threshold_otsu
import importlib
import numpy as np

models = importlib.import_module("tensorflow.keras.models")

filename = 'test.png'

img_original = mpimg.imread(filename)

# Ako slika ima RGBA format, makni alpha kanal
if len(img_original.shape) == 3 and img_original.shape[2] == 4:
    img_original = img_original[:, :, :3]

# Pretvori u grayscale ako je RGB
if len(img_original.shape) == 3:
    img = color.rgb2gray(img_original)
else:
    img = img_original

# Normalizacija raspona [0, 1]
img = img.astype("float32")
img = (img - img.min()) / (img.max() - img.min() + 1e-8)

# MNIST ima bijelu znamenku na crnoj pozadini.
# Ako je prosjek previše svijetao, invertirati.
if np.mean(img) > 0.5:
    img = 1.0 - img

# Binarizacija i izdvajanje znamenke (uklanjanje praznog prostora)
th = threshold_otsu(img)
mask = img > th

if np.any(mask):
    rows = np.where(mask.any(axis=1))[0]
    cols = np.where(mask.any(axis=0))[0]
    r0, r1 = rows[0], rows[-1]
    c0, c1 = cols[0], cols[-1]
    digit_crop = img[r0:r1 + 1, c0:c1 + 1]

    # Sačuvaj omjer stranica i smjesti znamenku u 20x20,
    # zatim je centriraj na 28x28 kao u MNIST preprocesiranju.
    h, w = digit_crop.shape
    if h > w:
        new_h = 20
        new_w = max(1, int(round(w * (20.0 / h))))
    else:
        new_w = 20
        new_h = max(1, int(round(h * (20.0 / w))))

    digit_resized = resize(digit_crop, (new_h, new_w), anti_aliasing=True)
    canvas = np.zeros((28, 28), dtype=np.float32)
    top = (28 - new_h) // 2
    left = (28 - new_w) // 2
    canvas[top:top + new_h, left:left + new_w] = digit_resized
    img = canvas
else:
    # Ako nema vidljive znamenke, ostavi prazno platno.
    img = np.zeros((28, 28), dtype=np.float32)

# Prikaži pripremljenu sliku
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.axis('off')
plt.title("Slika nakon pripreme")
plt.show()

# Pripremi sliku - ulaz u mrežu

img = img.reshape(1, 28, 28, 1)
img = img.astype('float32')

# Učitaj spremljenu mrežu

model = models.load_model("best_mnist_cnn.keras")

# Predikcija

prediction = model.predict(img)

predicted_class = np.argmax(prediction)
confidence = np.max(prediction) * 100

# Ispis rezultata

print("Vjerojatnosti po klasama:")
for i, prob in enumerate(prediction[0]):
    print(f"Znamenka {i}: {prob * 100:.2f}%")

print("\nPredviđena znamenka:", predicted_class)
print(f"Sigurnost modela: {confidence:.2f}%")

#Ako je znamenka centrirana, pravilne veličine i bez velike rotacije, model ju uglavnom dobro klasificira, ali miješa slične brojeve (npr 1 i 7, 3 i 8).

#Rotacija, različita debljina linije ili kriva pozadina mogu smanjiti točnost klasifikacije jer model nije treniran na takvim primjerima. 

#Pozicija na pozadini ne utječe toliko na klasifikaciju, isto kao i veličina znamenke - osim ako idemo u ekstreme - npr ako je znamenka jako mala, u pripremi ce biti dodatno "blurry".