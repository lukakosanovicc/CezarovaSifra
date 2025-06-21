# sifrovanje pomocu cezarove sifre (slova se pomeraju kljuc mesta unapred)

alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

def UnosKljuca():
    global kljuc
    kljuc = int(input("Unesite kljuc [1, 25]: "))
    while kljuc>25 or kljuc<1:
        print("Pogresan unos...")
        UnosKljuca()
def main():
    print()
    opcije = int(input("Da li zelite da 1. sifrujete ili 2. desifrujete? (ili unesite 0 za izlazak iz programa)\n>> "))
    if opcije == 0:
        return
    while opcije>2 or opcije<1:
        print("Pogresan unos...")
        main()
    if opcije == 1:
        string = input("Unesite recenicu za sifrovanje: ")
        UnosKljuca()
        string = string.upper()
        sifrovani_string = ""
        for i in string:
            if i in alfabet:
                indeks = alfabet.find(i)
                novi_indeks = indeks + kljuc
                sifrovani_string += alfabet[novi_indeks]
            else:
                sifrovani_string += i
        print("Vas sifrovani string je: ")
        print()
        print(sifrovani_string)
        main()
    elif opcije == 2:
        string = input("Unesite recenicu za desifrovanje: ")
        UnosKljuca()
        string = string.upper()
        desifrovani_string = ""
        for i in string:
            if i in alfabet:
                indeks = alfabet.find(i)
                novi_indeks = indeks - kljuc
                desifrovani_string += alfabet[novi_indeks]
            else:
                desifrovani_string += i
        print("Vas desifrovani string je: ")
        print()
        print(desifrovani_string)
        main()

if __name__ == "__main__":
    main()
