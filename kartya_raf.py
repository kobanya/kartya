import random
import tkinter as tk
from tkinter import messagebox

class Kartya:
    def __init__(self, szin, ertek):
        self.szin = szin
        self.ertek = ertek

    def __str__(self):
        return f"{self.szin}{self.ertek}"

class Pakli:
    def __init__(self):
        self.kartyak = []
        for szin, szin_kod in [("♠", "black"), ("♣", "black"), ("♦", "red"), ("♥", "red")]:
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

def keveres_button_click(pakli):
    try:
        pakli.keveres()
        messagebox.showinfo("Keveres", "A pakli keverve.")
    except ValueError as err:
        messagebox.showerror("Hiba", str(err))

def huzas_button_click(pakli, canvas, drawn_cards):
    try:
        kartya = pakli.huzas()
        #messagebox.showinfo("Huzas", f"Huzott kartya: {kartya}")
        draw_card(canvas, kartya, drawn_cards)
    except ValueError as err:
        messagebox.showerror("Hiba", str(err))

def draw_card(canvas, kartya, drawn_cards):
    x = 20 + (70 * (len(drawn_cards) % 26))  # X pozíció a kártya elhelyezéséhez
    y = 20 + (170 * (len(drawn_cards) // 26))  # Y pozíció a kártya elhelyezéséhez

    # Kártya háttére
    canvas.create_rectangle(x, y, x + 100, y + 160, fill="white")
    canvas.create_rectangle(x + 5, y + 5, x + 95, y + 155, fill="light gray")

    # Szín és érték
    szin = kartya.szin
    szin_szoveg = ""
    if szin == "♠" or szin == "♣":
        szin_szoveg = "black"
    else:
        szin_szoveg = "red"

    canvas.create_text(x + 50, y + 60, text=szin, font=("Arial", 36), fill=szin_szoveg)
    canvas.create_text(x + 50, y + 110, text=kartya.ertek, font=("Arial", 13), fill=szin_szoveg)

    drawn_cards.append(kartya)  # Kártya hozzáadása a húzott kártyákhoz

def main():
    pakli = Pakli()
    drawn_cards = []  # Húzott kártyák listája

    root = tk.Tk()
    root.title("Kartyajatek")

    canvas = tk.Canvas(root, width=2300, height=600)
    canvas.pack()

    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)

    keveres_button = tk.Button(button_frame, text="Keveres", command=lambda: keveres_button_click(pakli))
    keveres_button.pack(side="left", padx=200)

    huzas_button = tk.Button(button_frame, text="Huzas", command=lambda: huzas_button_click(pakli, canvas, drawn_cards))
    huzas_button.pack(side="left")

    root.mainloop()

if __name__ == "__main__":
    main()
