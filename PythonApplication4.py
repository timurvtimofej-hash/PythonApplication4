# # # PARANDUSED:
# # # 1. Parandatud jutumärgid, sulud, koolonid ja võrdlusmärgid.
# # # 2. Kõik kolmnurga küljed teisendatakse float-tüüpi arvudeks.
# # # 3. Parandatud kolmnurga olemasolu kontroll (kasutame AND-i).
# # # 4. Parandatud võrdkülgse ja võrdhaarse kolmnurga tingimused.
# # # 5. Lisatud külgede positiivsuse kontroll.
# # # 6. Lisatud täisnurkse kolmnurga kontroll Pythagorase teoreemiga.
# # # 7. Parandatud punktide vahemiku kontroll ja hinnete järjekord.
# # # 8. Parandatud pileti hinna tingimused.
# # # 9. Lisatud menüü, mille abil saab valida ühe programmi.


# # from re import I


# # print("Vali programm:")
# # print("1 - Kolmnurga kontroll")
# # print("2 - Hinde arvutamine")
# # print("3 - Pileti hind")

# # valik = input("Sisesta valik (1-3) => ")

# # # KOLMNURGA KONTROLL
# # if valik == "1":
# #     print("Kolmnurga kontroll")

# #     a = float(input("Sisesta 1. külje pikkus => "))
# #     b = float(input("Sisesta 2. külje pikkus => "))
# #     c = float(input("Sisesta 3. külje pikkus => "))

# #     # Kontrollime, et kõik küljed oleksid positiivsed.
# #     if a <= 0 or b <= 0 or c <= 0:
# #         print("Külgede pikkused peavad olema positiivsed!")

# #     # Kontrollime, kas selline kolmnurk saab olemas olla.
# #     elif a + b > c and a + c > b and b + c > a:
# #         print("Kolmnurk on olemas")

# #         # Kolmnurga liigi kontroll.
# #         if a == b and b == c:
# #             print("Kolmnurk on võrdkülgne")
# #         elif a == b or b == c or a == c:
# #             print("Kolmnurk on võrdhaarne")
# #         else:
# #             print("Kolmnurk on erikülgne")

# #         # Kontrollime Pythagorase teoreemi abil,
# #         # kas kolmnurk on täisnurkne.
# #         kyljed = sorted([a, b, c])

# #         if abs(kyljed[0] ** 2 + kyljed[1] ** 2 - kyljed[2] ** 2) < 0.000001:
# #             print("Kolmnurk on täisnurkne")

# #     else:
# #         print("Sellist kolmnurka ei ole olemas")

# # # HINDE ARVUTAMINE
# # elif valik == "2":
# #     print("Hinde arvutamine")

# #     punktid = int(input("Sisesta punktide arv (0-100) => "))

# #     # Kontrollime, kas punktide arv on lubatud vahemikus.
# #     if punktid < 0 or punktid > 100:
# #         print("Vigane punktide arv")

# #     # Kõrgemaid hindeid kontrollime kõigepealt.
# #     elif punktid >= 90:
# #         print("Hinne: 5")
# #     elif punktid >= 75:
# #         print("Hinne: 4")
# #     elif punktid >= 50:
# #         print("Hinne: 3")
# #     else:
# #         print("Hinne: 2")

# # # PILETI HIND
# # elif valik == "3":
# #     print("Pileti hind")

# #     vanus = int(input("Sisesta oma vanus => "))

# #     # Alla 7-aastastele on pilet tasuta.
# #     if vanus < 0:
# #         print("Vigane vanus")
# #     elif vanus < 7:
# #         print("Pilet on tasuta")

# #     # 7-18-aastastele ja vähemalt 65-aastastele on sooduspilet.
# #     elif 7 <= vanus <= 18 or vanus >= 65:
# #         print("Pileti hind on 3 €")

# #     else:
# #         print("Pileti hind on 6 €")

# # # Kui kasutaja ei vali 1, 2 ega 3.
# # else:
# #     print("Vigane valik")
# # ##
# # print(" *_* ")
# # # while True:
# # #     print("\nTee valik: ")
# # #     print("1. while-tsükkel")
# # #     print("2. while True ja break")
# # #     print("3. for-tsükkel")
# # #     print("4. summa ja keskmine")
# # #     print("5. loendamine ja suurim")
# # #     print("0. Välju")

# # #     valik = input("Vali tegevus: ")
# # #     if valik == "0":
# # #         break
# # #     elif valik == "1":
# # #         # 1. while-tsükkel
# # #             x = 0
# # #             while x < 30:
# # #                 if x % 2 == 1:
# # #                     print(x, end=" ")
# # #                 x += 1
# # #     elif valik == "2":
# # #         #2. while True ja break
# # #         x = 0
# # #         while True:
# # #             if x % 2 == 1:
# # #                 print(x, end=" ")
# # #             if x == 30:
# # #                 break
# # #             x += 1
# # #     elif valik == "3":
# # #         #3. for-tsükkel
# # #         for i in range(1, 31, 2):
# # #             print(i, end=" ")
# # #     elif valik == "4":
# # #         #4. Summa ja keskmine
# # #         N = int(input("N: "))
# # #         summa = 0
# # #         i = 1
# # #         while i <= N:
# # #             summa = summa + i
# # #             i = i + 1
# # #         print("Summa:", summa)
# # #         print("Keskmine:", summa / N)
# # #     elif valik == "5":
# # #         #5. Loendamine ja suurim
# # #         kogus = 0
# # #         suurim = None
# # #         for i in range(5):
# # #             arv = float(input(f"{i + 1}. arv: "))
# # #             if arv > 0:
# # #                 kogus += 1
# # #             if suurim is None or arv > suurim:
# # #                 suurim = arv
# # #         print("Positiivseid arve:", kogus)
# # #         print("Suurim arv:", suurim)
# # #     else:
# # #         print("Vale valik!")  
# 1️
# Sisestatakse 15 arvu.
# Määrata, mitu neist on täisarvud.
for i in range(15):
    try:
        arv=float(input(f"{i+1}. arv: "))
        if arv.is_integer():
            print(f"{arv}on täisarv.")
        else:
            print(f"{arv} ei ole täisarv.")
    except ValueError:
        print("Palun sisestega arv.")

#while kasutades
i = 0
while i < 15:
    try:
        arv = float(input(f"{i + 1}. arv: "))
        if arv.is_integer():
            print(f"{arv} on täisarv.")
        else:
            print(f"{arv} ei ole täisarv.")
        i += 1 # arvu lugemine,ainult siis kui sisestus on õige
        if i==15:
            break
    except ValueError:
        print("Palun sisestage arv.")
# 2️
# Küsi kasutajalt arv A ja
# leia kõigi naturaalarvude summa vahemikus 1 kuni A.
#for kasutades
try:
    A = int(input("Sisesta arv A: "))
    summa = 0
    for i in range(1, A + 1):
        summa += i
    print(f"Summa vahemikus 1 kuni {A} on {summa}.")
except ValueError:
    print("Palun sisestage täisarv.")

# 3️
# Sisestatakse 8 arvu.
# Leida nende korrutis (ainult positiivsete arvude puhul).
# # try:
# #     korrutis = 1

# #     for i in range(8):
# #         arv = float(input("Sisesta arv: "))
# #         if arv > 0:
# #             korrutis *= arv

# #     print(f"Positiivsete arvude korrutis on {korrutis}.")

# # except ValueError:
# #     print("Palun sisestage arv.") #või
korrutis=1
for i in range(8):
    try:
        arv = float(input(f"{i + 1}. arv: "))
        if arv > 0:
            korrutis *= arv
    except ValueError:
        print("Palun sisestaga arv.")
print(f"Posittiivsete arvude korrutis on {korrutis}.")
#4️
#Koosta programm, mis väljastab ekraanile 
#arvude ruudud vahemikus 10 kuni 20. 10^2, 11^2, 12^2, ...,20^2
#for
for i in range(10, 21):
    print(f"{i}^2 = {i**2}")
#while
i = 10
while i <= 20:
    print(f"{i}^2 = {i**2}")
    i += 1
#5️
# Koosta programm, mis arvutab ainult negatiivsete arvude summa N sisestatud arvu seast.
# N väärtus sisestatakse klaviatuurilt.
try:
    N = int(input("Sisesta arv N: "))
    summa = 0

    for i in range(N):
        arv = float(input("Sisesta arv: "))
        if arv < 0:
            summa += arv

    print(f"Negatiivsete arvude summa on {summa}.")

except ValueError:
    print("Palun sisestage arv.")
# 6️
# Klaviatuurilt sisestatakse N arvu.
# Koosta programm, mis määrab sisestatud arvude seast:
# negatiivsete arvude arvu,
# positiivsete arvude arvu,
# nullide arvu.
# (N väärtus sisestatakse klaviatuurilt.)
try:
    N = int(input("Sisesta arvude kogus N: "))
    negatiivsed = 0
    positiivsed = 0
    nullid = 0
    for i in range(N):
        try:
            arv = float(input(f"{i + 1}. arv: "))
            if arv < 0:
                negatiivsed += 1
            elif arv > 0:
                positiivsed += 1
            else:
                nullid += 1
        except ValueError:
            print("Palun sisestage arv.")
    print(f"Negatiivsete arvude arv: {negatiivsed}")
    print(f"Positiivsete arvude arv: {positiivsed}")
    print(f"Nullide arv: {nullid}")
except ValueError:
    print("Palun sisestage täisarv.")
