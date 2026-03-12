# Napišite Python skriptu koja će učitati tekstualnu datoteku naziva song.txt. Potrebno je napraviti rječnik koji kao ključeve koristi sve različite riječi koje se pojavljuju u datoteci,
# dok su vrijednosti jednake broju puta koliko se svaka riječ (ključ) pojavljuje u datoteci. Koliko je riječi koje se pojavljuju samo jednom u datoteci? 
# Ispišite ih.

rjecnik = {}
naziv_datoteke = input("Ime datoteke: ")
datoteka = open(naziv_datoteke, 'r')
for linija in datoteka:
        rijeci = linija.split()

        for rijec in rijeci:
            if rijec in rjecnik:
                rjecnik[rijec] += 1
            else:
                rjecnik[rijec] = 1

print(rjecnik)
datoteka.close



