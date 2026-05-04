import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans
from skimage import data

face = data.camera()
X1 = face.reshape((-1, 1))

kmeans1 = KMeans(n_clusters=5, n_init=10, random_state=0)
kmeans1.fit(X1)

values1 = kmeans1.cluster_centers_.squeeze()
labels1 = kmeans1.labels_

face_compressed = np.choose(labels1, values1)
face_compressed.shape = face.shape

plt.figure()
plt.imshow(face, cmap='gray')
plt.title("Original - camera")
plt.axis('off')

plt.figure()
plt.imshow(face_compressed, cmap='gray')
plt.title("Kvantizirana - camera")
plt.axis('off')

plt.show()

# -------------------------
#  SLIKA IZ ZADATKA
# -------------------------
imageNew = mpimg.imread(r'C:\Users\student\Desktop\LV6_ms\example_grayscale.png')


if len(imageNew.shape) == 3:
    imageNew = imageNew.mean(axis=2)

X2 = imageNew.reshape((-1, 1))

k = 10
kmeans2 = KMeans(n_clusters=k, n_init=10, random_state=0)
kmeans2.fit(X2)

values2 = kmeans2.cluster_centers_.squeeze()
labels2 = kmeans2.labels_

image_compressed = np.choose(labels2, values2)
image_compressed.shape = imageNew.shape

plt.figure()
plt.imshow(imageNew, cmap='gray')
plt.title("Original - example")
plt.axis('off')

plt.figure()
plt.imshow(image_compressed, cmap='gray')
plt.title(f"Kvantizirana ({k} klastera)")
plt.axis('off')

plt.show()