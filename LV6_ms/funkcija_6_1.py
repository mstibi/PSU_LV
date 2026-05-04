from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

def generate_data(n_samples, flagc):
    
    if flagc == 1:
        random_state = 365
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        
    elif flagc == 2:
        random_state = 148
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
        X = np.dot(X, transformation)
        
    elif flagc == 3:
        random_state = 148
        X, y = datasets.make_blobs(n_samples=n_samples,
                                    centers=4,
                                    cluster_std=[1.0, 2.5, 0.5, 3.0],
                                    random_state=random_state)

    elif flagc == 4:
        X, y = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.05)
        
    elif flagc == 5:
        X, y = datasets.make_moons(n_samples=n_samples, noise=.05)
    
    else:
        X = []
        
    return X



X = generate_data(500, 1)  



# kmeans = KMeans(n_clusters=3, n_init=10)


# kmeans.fit(X)


# labels = kmeans.predict(X)


# centers = kmeans.cluster_centers_


# plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=30)
# plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, marker='X')
# plt.title("K-means grupiranje")
# plt.show()



# inertia_values = []
# K = range(1, 21)

# for k in K:
#     kmeans = KMeans(n_clusters=k, n_init=10)
#     kmeans.fit(X)
#     inertia_values.append(kmeans.inertia_)

# plt.plot(K, inertia_values, marker='o')
# plt.xlabel("Broj klastera (k)")
# plt.ylabel("Vrijednost kriterijske funkcije (inertia)")
# plt.title("Elbow metoda")
# plt.show()

Z = linkage(X, method='average')  

# dendrogram
plt.figure(figsize=(10, 5))
dendrogram(Z)
plt.title("Dendrogram")
plt.xlabel("Podaci")
plt.ylabel("Udaljenost")
plt.show()