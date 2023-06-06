import random
import tkinter as tk
from tkinter import messagebox

CARD_WIDTH = 100
CARD_HEIGHT = 160

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
            random.SystemRandom().shuffle(self.kartyak)
        else:
            raise ValueError("Megkezdett pakli nem keverheto")

    def huzas(self):
        if len(self.kartyak) == 0:
            raise ValueError("Nincs tobb kartya a pakliban")
        index = random.randint(0, len(self.kartyak) - 1)
        return self.kartyak.pop(index)

def keveres_button_click(pakli, canvas, drawn_cards):
    try:
        pakli.keveres()
        drawn_cards.clear()
        draw_deck(canvas, pakli, drawn_cards)
    except ValueError as err:
        messagebox.showerror("Hiba", str(err))

def draw_deck(canvas, pakli, drawn_cards):
    canvas.delete("deck")
    x = 20
    y = 20
    for i, kartya in enumerate(pakli.kartyak):
        if i % 13 == 0 and i != 0:
            x = 20
            y += CARD_HEIGHT + 10
        if kartya not in drawn_cards:
            draw_card(canvas, kartya, x, y, drawn_cards, False)
        x += CARD_WIDTH + 10

def huzas_button_click(pakli, canvas, drawn_cards):
    try:
        kartya = pakli.huzas()
        drawn_cards.clear()
        remove_card(canvas)
        draw_deck(canvas, pakli, drawn_cards)
        draw_card(canvas, kartya, 1700, 20, drawn_cards)
        if len(drawn_cards) > 26:
            drawn_cards.pop(0)
    except ValueError as err:
        messagebox.showerror("Hiba", str(err))

def reset_game(canvas, pakli, drawn_cards):
    pakli.__init__()
    drawn_cards.clear()
    remove_card(canvas)
    draw_deck(canvas, pakli, drawn_cards)

def remove_card(canvas):
    canvas.delete("card")

def draw_card(canvas, kartya, x, y, drawn_cards, new_card=True):
    canvas.create_rectangle(x, y, x + CARD_WIDTH, y + CARD_HEIGHT, fill="white", tags="card")
    canvas.create_rectangle(x + 5, y + 5, x + CARD_WIDTH - 5, y + CARD_HEIGHT - 5, fill="light gray", tags="card")
    szin = kartya.szin
    szin_szoveg = "black" if szin == "♠" or szin == "♣" else "red"
    canvas.create_text(x + (CARD_WIDTH // 2), y + (CARD_HEIGHT // 2) - 40, text=szin, font=("Arial", 48), fill=szin_szoveg, tags="card")
    canvas.create_text(x + (CARD_WIDTH // 2), y + (CARD_HEIGHT // 2) + 30, text=kartya.ertek, font=("Arial", 13), fill=szin_szoveg, tags="card")
    if new_card:
        drawn_cards.append(kartya)

def main():
    pakli = Pakli()
    drawn_cards = []

    root = tk.Tk()
    root.title("Kártyajáték")

    canvas = tk.Canvas(root, width=2000, height=1000)
    canvas.pack()

    deck_frame = tk.Frame(root)
    deck_frame.pack(pady=20)

    keveres_button = tk.Button(deck_frame, text="Keverés", command=lambda: keveres_button_click(pakli, canvas, drawn_cards))
    keveres_button.pack(side="left", padx=10)

    huzas_button = tk.Button(deck_frame, text="Húzás", command=lambda: huzas_button_click(pakli, canvas, drawn_cards))
    huzas_button.pack(side="left", padx=10)

    uj_jatek_button = tk.Button(deck_frame, text="ÚJ JÁTÉK", command=lambda: reset_game(canvas, pakli, drawn_cards))
    uj_jatek_button.pack(side="left", padx=10)

    draw_deck(canvas, pakli, drawn_cards)

    root.mainloop()

if __name__ == "__main__":
    main()
