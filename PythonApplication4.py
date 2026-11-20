# PARANDUSED:
# 1. Parandatud jutumärgid, sulud, koolonid ja võrdlusmärgid.
# 2. Kõik kolmnurga küljed teisendatakse float-tüüpi arvudeks.
# 3. Parandatud kolmnurga olemasolu kontroll (kasutame AND-i).
# 4. Parandatud võrdkülgse ja võrdhaarse kolmnurga tingimused.
# 5. Lisatud külgede positiivsuse kontroll.
# 6. Lisatud täisnurkse kolmnurga kontroll Pythagorase teoreemiga.
# 7. Parandatud punktide vahemiku kontroll ja hinnete järjekord.
# 8. Parandatud pileti hinna tingimused.
# 9. Lisatud menüü, mille abil saab valida ühe programmi.


from re import I


print("Vali programm:")
print("1 - Kolmnurga kontroll")
print("2 - Hinde arvutamine")
print("3 - Pileti hind")

valik = input("Sisesta valik (1-3) => ")

# KOLMNURGA KONTROLL
if valik == "1":
    print("Kolmnurga kontroll")

    a = float(input("Sisesta 1. külje pikkus => "))
    b = float(input("Sisesta 2. külje pikkus => "))
    c = float(input("Sisesta 3. külje pikkus => "))

    # Kontrollime, et kõik küljed oleksid positiivsed.
    if a <= 0 or b <= 0 or c <= 0:
        print("Külgede pikkused peavad olema positiivsed!")

    # Kontrollime, kas selline kolmnurk saab olemas olla.
    elif a + b > c and a + c > b and b + c > a:
        print("Kolmnurk on olemas")

        # Kolmnurga liigi kontroll.
        if a == b and b == c:
            print("Kolmnurk on võrdkülgne")
        elif a == b or b == c or a == c:
            print("Kolmnurk on võrdhaarne")
        else:
            print("Kolmnurk on erikülgne")

        # Kontrollime Pythagorase teoreemi abil,
        # kas kolmnurk on täisnurkne.
        kyljed = sorted([a, b, c])

        if abs(kyljed[0] ** 2 + kyljed[1] ** 2 - kyljed[2] ** 2) < 0.000001:
            print("Kolmnurk on täisnurkne")

    else:
        print("Sellist kolmnurka ei ole olemas")

# HINDE ARVUTAMINE
elif valik == "2":
    print("Hinde arvutamine")

    punktid = int(input("Sisesta punktide arv (0-100) => "))

    # Kontrollime, kas punktide arv on lubatud vahemikus.
    if punktid < 0 or punktid > 100:
        print("Vigane punktide arv")

    # Kõrgemaid hindeid kontrollime kõigepealt.
    elif punktid >= 90:
        print("Hinne: 5")
    elif punktid >= 75:
        print("Hinne: 4")
    elif punktid >= 50:
        print("Hinne: 3")
    else:
        print("Hinne: 2")

# PILETI HIND
elif valik == "3":
    print("Pileti hind")

    vanus = int(input("Sisesta oma vanus => "))

    # Alla 7-aastastele on pilet tasuta.
    if vanus < 0:
        print("Vigane vanus")
    elif vanus < 7:
        print("Pilet on tasuta")

    # 7-18-aastastele ja vähemalt 65-aastastele on sooduspilet.
    elif 7 <= vanus <= 18 or vanus >= 65:
        print("Pileti hind on 3 €")

    else:
        print("Pileti hind on 6 €")


# Kui kasutaja ei vali 1, 2 ega 3.
else:
    print("Vigane valik")
##
print(" *_* ")