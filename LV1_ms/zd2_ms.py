# Napišite program koji od korisnika zahtijeva upis jednog broja koji predstavlja nekakvu ocjenu i nalazi se između 0.0 i 1.0. 
# Ispišite kojoj kategoriji pripada ocjena na temelju sljedećih uvjeta:
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# Ako korisnik nije utipkao broj, ispišite na ekran poruku o grešci (koristite try i except naredbe). 
# Također, ako je broj izvan intervala [0.0 i 1.0] potrebno je ispisati odgovarajuću poruku.

while True:
    try:
        x = float(input("Unesi ocjenu: "))
        if x < 0 or x > 1:
            print("Greška, unesi ponovno ocjenu: ")
            continue
        if x >= 0.9:
            print("A")
        elif x >= 0.8:
            print("B")
        elif x >= 0.7:
            print("C")
        elif x >= 0.6:
            print("D")
        elif x < 0.6:
            print("F")
        break
    except:
        print("Niste unijeli broj")


