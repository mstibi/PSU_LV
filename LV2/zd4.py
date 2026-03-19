import numpy as np
import matplotlib.pyplot as plt

def bw_polje(velicina_kv, broj_kv_visina, broj_kv_sirina):

    crni = np.zeros((velicina_kv, velicina_kv), dtype=np.uint8)
    bijeli = np.ones((velicina_kv, velicina_kv), dtype=np.uint8) * 255

    redovi = []
    for i in range(broj_kv_visina):
        kvadrati_u_redu = []
        for j in range(broj_kv_sirina):
          
            if (i + j) % 2 == 0:
                kvadrati_u_redu.append(crni)
            else:
                kvadrati_u_redu.append(bijeli)

        red = np.hstack(kvadrati_u_redu)
        redovi.append(red)

    slika = np.vstack(redovi)
    return slika

vel_kvadrata = int(input("Unesi velicinu kvadrata u pixelima "))
visina = int(input("Unesi visinu kvadrata "))
sirina = int(input("Unesi sirinu kvadrata "))


img = bw_polje(vel_kvadrata, visina, sirina)

plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.axis('off')
plt.show()