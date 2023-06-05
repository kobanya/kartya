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
        for szin in ["♠", "♣", "♦", "♥"]:
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

def huzas_button_click(pakli, canvas):
    try:
        kartya = pakli.huzas()
       # messagebox.showinfo("Huzas", f"Huzott kartya: {kartya}")
        draw_card(canvas, kartya)
    except ValueError as err:
        messagebox.showerror("Hiba", str(err))

def draw_card(canvas, kartya):
    canvas.delete("all")

    # Kártya háttére
    canvas.create_rectangle(20, 20, 120, 180, fill="white")
    canvas.create_rectangle(25, 25, 115, 175, fill="light gray")

    # Szín és érték
    canvas.create_text(70, 70, text=kartya.szin, font=("Arial", 48), fill="black")
    canvas.create_text(70, 150, text=kartya.ertek, font=("Arial", 13), fill="black")

def main():
    pakli = Pakli()

    root = tk.Tk()
    root.title("Kartyajatek")

    canvas = tk.Canvas(root, width=2400, height=400)
    canvas.pack()

    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)

    keveres_button = tk.Button(button_frame, text="Keveres", command=lambda: keveres_button_click(pakli))
    keveres_button.pack(side="left", padx=150)

    huzas_button = tk.Button(button_frame, text="Huzas", command=lambda: huzas_button_click(pakli, canvas))
    huzas_button.pack(side="left")

    root.mainloop()

if __name__ == "__main__":
    main()
