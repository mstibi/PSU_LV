import os
import numpy as np
import matplotlib.pyplot as plt

folder = os.path.dirname(__file__)

data = np.loadtxt(open(os.path.join(folder, "mtcars.csv"), "rb"),
                  usecols=(1, 2, 3, 4, 5, 6), delimiter=",", skiprows=1)

mpg = data[:, 0]
cyl = data[:, 1]
hp  = data[:, 3]
wt  = data[:, 5]

plt.scatter(hp, mpg, s=wt * 40, alpha=0.7)
plt.xlabel("Konjske snage (hp)")
plt.ylabel("Potrošnja (mpg)")
plt.title("Ovisnost potrošnje o konjskim snagama")
plt.show()

print("Sve vrijednosti (mpg)")
print(f"  Min:  {mpg.min()}")
print(f"  Max:  {mpg.max()}")
print(f"  Mean: {mpg.mean():.2f}")

mpg_6cyl = mpg[cyl == 8]
print("\nAutomobili sa 6 cilindara (mpg)")
print(f"  Min:  {mpg_6cyl.min()}")
print(f"  Max:  {mpg_6cyl.max()}")
print(f"  Mean: {mpg_6cyl.mean():.2f}")

print(hp.shape)
print(hp.mean())
