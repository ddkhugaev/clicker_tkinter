import tkinter as tk
from tkinter import ttk

# глобальные переменные программы
money = 0
power = 1
cost = 10

# создание окна
root = tk.Tk()
root.title("clicker")
root.geometry("400x300")

# отображение денег
money_label = ttk.Label(root, text="кликните, чтобы начать")
money_label.pack()


# кнопка клика
def click():
    global money

    money += power
    money_label.configure(text=money)


click_button = ttk.Button(root, text="клик", command=click)
click_button.pack()


# кнопка улучшения
def upgrade():
    global money
    global cost
    global power

    if money >= cost:
        money -= cost
        cost *= 2
        power += 1
        money_label.configure(text=money)
        upgrade_button.configure(text=f"улучшить (цена {cost})")


upgrade_button = ttk.Button(root, text=f"улучшить (цена {cost})", command=upgrade)
upgrade_button.pack()

# запск приложения
root.mainloop()
