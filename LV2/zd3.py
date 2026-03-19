import os
import numpy as np
import matplotlib.pyplot as plt

img = plt.imread(os.path.join(os.path.dirname(__file__), "tiger.png"))

brightness = 0.3
img_bright = np.clip(img + brightness, 0, 1)

img_rot = np.rot90(img, k=-1)
img_mirror = np.fliplr(img)


img_lowres = img[::10, ::10, ...]

h, w = img.shape[:2]
x1 = w // 4
x2 = w // 2
img_q2 = np.zeros_like(img)
img_q2[:, x1:x2, ...] = img[:, x1:x2, ...]

fig, axes = plt.subplots(2, 3, figsize=(12, 8))

axes[0, 0].imshow(img)
axes[0, 0].set_title("Originalna slika")

axes[0, 1].imshow(img_bright)
axes[0, 1].set_title(f"Posvijetljena (+{brightness})")

axes[0, 2].imshow(img_rot)
axes[0, 2].set_title("Rotirana 90° (clockwise)")

axes[1, 0].imshow(img_mirror)
axes[1, 0].set_title("Zrcaljena slika")

axes[1, 1].imshow(img_lowres, interpolation="nearest")
axes[1, 1].set_title("Low-res (10x manje)")

axes[1, 2].imshow(img_q2)
axes[1, 2].set_title("Samo 2. cetvrtina po sirini")

plt.tight_layout()
plt.show()