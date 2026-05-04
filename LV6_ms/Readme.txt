Zadatak 1.

Primjećujem da se centri klastera mogu pojaviti na drugačijim mjestima, to je zato što kmeans metoda odabire nasumično pozicije centara + rezultat jako ovisi o obliku podataka:

flagc = 1 (jednostavni, jasno odvojeni klasteri) - K-means radi odlično, klasteri su pravilno prepoznati

flagc = 2 (linearno transformirani podaci) - i dalje radi dobro, ali granice nisu savršene

flagc = 3 (različite varijance klastera) - K-means može pogriješiti jer pretpostavlja klastere slične veličine

flagc = 4 (koncentrični krugovi) - K-means ne daje dobre rezultate, dijeli podatke "pogrešno" jer ne može prepoznati kružnu strukturu

flagc = 5 (polumjeseci) - opet loš rezultat jer klasteri nisu linearno odvojivi


Zadatak 2.

Vrijednost kriterijske funkcije uvijek opada kako povećavamo broj klaster, jer više klastera = manja udaljenost točaka od centara	
	
Pad je velik na početku, a kasnije postaje sve manji. 

Optimalan broj klastera određujem pomoću metode lakta kao vrijednost k u kojoj dolazi do nagle promjene nagiba krivulje. 
U toj točki daljnje povećanje broja klastera ne donosi značajno smanjenje kriterijske funkcije.


Zadatak 3.

Dendrogram prikazuje hijerarhijsko spajanje podataka u klastere. Promjenom metode spajanja dobivaju se različiti rezultati. Metoda ward daje najkompaktnije i najprirodnije klastere, dok metoda single pokazuje chaining efekt i lošije razdvaja klastere. Metoda complete daje kompaktnije klastere od single, a metoda average je nekakav kompromis između metoda single i complete. Optimalan broj klastera može se odrediti kao broj grana koje se presijecaju horizontalnom linijom postavljenom na mjestu najvećeg skoka u udaljenosti.


Zadatak 4.

Primjenom K-means algoritma za kvantizaciju slike smanjuje se broj mogućih nijansi sive na 10 klastera, što dovodi do gubitka finih detalja i pojave vidljivih prijelaza između tonova.

Originalna: log2​(256)=8 bita po pikselu
Kvantizirana: log2​(10)=3.32 bita po pikselu

Originalna slika koristi 8 bita po pikselu, dok kvantizirana slika koristi približno 3.32 bita po pikselu. Time se postiže kompresija od oko 2.4 puta u odnosu na originalnu sliku.

