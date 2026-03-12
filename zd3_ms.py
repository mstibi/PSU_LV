# Napišite program koji od korisnika zahtijeva unos brojeva u beskonačnoj petlji sve dok korisnik ne upiše „Done" (bez navodnika). 
# Pri tome brojeve spremajte u listu. Nakon toga potrebno je ispisati koliko brojeva je korisnik unio, njihovu srednju, 
# minimalnu i maksimalnu vrijednost. Sortirajte listu i ispišite je na ekran.
# Dodatno: osigurajte program od pogrešnog unosa (npr. slovo umjesto brojke) na način da program zanemari taj unos i ispiše odgovarajuću poruku.

lista = []

while True:
    unos = input("Unesite broj (ili 'Done' za završetak): ")
    
    if unos == "Done":
        break
    
    try:
        broj = float(unos)
        lista.append(broj)
    except ValueError:
        print("Greška: Molimo unesite validan broj!")


if len(lista) > 0:
    print(f"\nBroj unesenih brojeva: {len(lista)}")
    print(f"Prosječna vrijednost: {sum(lista) / len(lista):.2f}")
    print(f"Minimalna vrijednost: {min(lista)}")
    print(f"Maksimalna vrijednost: {max(lista)}")
    
    lista.sort()
    print(f"Sortirana lista: {lista}")
else:
    print("Niste unijeli nikakve brojeve!")