
naziv = "SMSSpamCollection.txt"

try:
    with open(naziv, "r", encoding="utf-8") as dat:
        ham_count = spam_count = 0          
        ham_words = spam_words = 0          
        spam_exclaim = 0                   
        
        for line in dat:
            line = line.strip()
            if not line:
                continue
            # format: "<tip>\t<tekst>"
            parts = line.split("\t", 1)
            if len(parts) != 2:
                continue
            tip, tekst = parts
            rijeci = tekst.split()
            
            if tip == "ham":
                ham_count += 1
                ham_words += len(rijeci)
            elif tip == "spam":
                spam_count += 1
                spam_words += len(rijeci)
                if tekst.endswith("!"):
                    spam_exclaim += 1

    # a) prosjek riječi
    if ham_count:
        print(f"Prosječan broj riječi u ham porukama: {ham_words/ham_count:.2f}")
    if spam_count:
        print(f"Prosječan broj riječi u spam porukama: {spam_words/spam_count:.2f}")

    # b) spam poruka s uskličnikom
    print(f"Spam poruka koje završavaju uskličnikom: {spam_exclaim}")

except FileNotFoundError:
    print(f"Datoteka {naziv} nije pronađena.")