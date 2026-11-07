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

# создание стилей
style = ttk.Style()
style.theme_use("clam")
style.configure("Gold.TButton", background="gold")
style.configure("Red.TButton", background="red")
style.configure("Green.TButton", background="green")

# отображение денег
money_label = ttk.Label(root, text="кликните, чтобы начать")
money_label.pack(padx=10, pady=10)


# обновление стилей
def update_style():
    # цвет фона кнопки улучшения
    if money >= cost:
        upgrade_button.configure(style="Green.TButton")
    else:
        upgrade_button.configure(style="Red.TButton")


# кнопка клика
def click():
    global money

    money += power
    money_label.configure(text=money)

    update_style()


click_button = ttk.Button(root, text="клик", command=click, style="Gold.TButton")
click_button.pack(padx=10, pady=10)


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

    update_style()


upgrade_button = ttk.Button(root, text=f"улучшить (цена {cost})", command=upgrade, style="Red.TButton")
upgrade_button.pack(padx=10, pady=10)

# запск приложения
root.mainloop()
