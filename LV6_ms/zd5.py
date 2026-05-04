import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans

image = mpimg.imread(r'C:\Users\student\Desktop\LV6_ms\example.png')


if image.max() > 1:
    image = image / 255.0

X = image.reshape(-1, 3)

kmeans = KMeans(n_clusters=10, n_init=10, random_state=0)
kmeans.fit(X)

labels = kmeans.labels_
centers = kmeans.cluster_centers_

image_q = centers[labels].reshape(image.shape)

# ORIGINAL
plt.figure()
plt.imshow(image)
plt.title("Original")
plt.axis('off')

# KVANTIZIRANA
plt.figure()
plt.imshow(np.clip(image_q, 0, 1))
plt.title("Kvantizirana")
plt.axis('off')

plt.show()

#Sto vise stavim clustera, to će slika izgledati "sličnije" originalu