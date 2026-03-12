# Napišite program koji od korisnika zahtijeva unos imena tekstualne datoteke. Program nakon toga treba tražiti linije oblika:
# Primijenjeno strojno učenje – laboratorijske vježbe – VJEŽBA 1 7
# X-DSPAM-Confidence: <neki_broj>
# koje predstavljaju pouzdanost korištenog spam filtra. Potrebno je izračunati srednju vrijednost pouzdanosti. Koristite datoteke mbox.txt i mbox-short.txt
# Primjer
# Ime datoteke: mbox.txt
# Average X-DSPAM-Confidence: 0.894128046745
# Ime datoteke: mbox-short.txt
# Average X-DSPAM-Confidence: 0.750718518519

# Program za pronalaženje srednje vrijednosti X-DSPAM-Confidence

naziv_datoteke = input("Ime datoteke: ")

try:
    datoteka = open(naziv_datoteke, 'r')
    suma = 0
    broj_linija = 0
    
    for linija in datoteka:
        if linija.startswith("X-DSPAM-Confidence:"):
            broj = float(linija.split(":")[1])
            suma += broj
            broj_linija += 1
    
    datoteka.close()
    
    if broj_linija > 0:
        prosjek = suma / broj_linija
        print(f"Average X-DSPAM-Confidence: {prosjek}")
    else:
        print("Nema pronađenih X-DSPAM-Confidence linija!")
        
except FileNotFoundError:
    print(f"Datoteka '{naziv_datoteke}' nije pronađena!")
except ValueError:
    print("Greška pri čitanju broja iz datoteke!")