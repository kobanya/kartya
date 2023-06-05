

import random


def menu():
    pakli = Pakli()

    while True:
        print("\n--- MENU ---")
        print("1 - Keveres")
        print("2 - Huzas")
        print("0 - Kilepes")

        try:
            valasz = int(input("Valassz egy menupontot: "))
        except ValueError:
            print("Ervenytelen valasz. Probald ujra.")
            continue

        match valasz:
            case 1:
                try:
                    pakli.keveres()
                    print("A pakli keverve.")
                    print(pakli)
                except ValueError as err:
                    print(str(err))
            case 2:
                try:
                    kartya = pakli.huzas()
                    print(f"Huzott kartya: {kartya}")
                    print(pakli)
                except ValueError as err:
                    print(str(err))
            case 0:
                print("Viszlat!")
                break
            case _:
                print("Ervenytelen valasz. Probald ujra.")




class Kartya:
    def __init__(self, szin, ertek):
        self.szin = szin
        self.ertek = ertek

    def __str__(self):
        return f"{self.szin}{self.ertek}"

class Pakli:
    def __init__(self):
        self.kartyak = []
        for szin in ["pikk", "kor", "karo", "treff"]:
            for ertek in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
                self.kartyak.append(Kartya(szin, ertek))

    def __str__(self):
        return " ".join([str(kartya) for kartya in self.kartyak])

    def keveres(self):
        if len(self.kartyak) == 52:
            random.shuffle(self.kartyak)
        else:
            raise ValueError("Megkezdett pakli nem keverheto")

    def huzas(self):
        if len(self.kartyak) == 0:
            raise ValueError("Nincs tobb kartya a pakliban")
        return self.kartyak.pop()



menu()
