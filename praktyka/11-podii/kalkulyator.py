"""Робота 11: заготовка калькулятора. Скопіюйте у kalkulyator.py і працюйте там:
    copy praktyka/11-podii/zahotovka_kalkulyator.py praktyka/11-podii/kalkulyator.py

Макет (тема 10) уже готовий. Ваше завдання — ПОВЕДІНКА: функції й звʼязування подій.
Перевірка:  python praktyka/11-podii/perevir.py
"""
import tkinter as tk

vikno = tk.Tk()
vikno.title("Калькулятор")

tk.Label(vikno, text="Перше:").grid(row=0, column=0, sticky="e", padx=8, pady=4)
pole_a = tk.Entry(vikno, width=14)
pole_a.grid(row=0, column=1, padx=8)

tk.Label(vikno, text="Друге:").grid(row=1, column=0, sticky="e", padx=8, pady=4)
pole_b = tk.Entry(vikno, width=14)
pole_b.grid(row=1, column=1, padx=8)

operatsiia = tk.StringVar(value="+")
ramka = tk.Frame(vikno)
ramka.grid(row=2, column=0, columnspan=2)
for znak in ("+", "−", "×", "÷"):
    tk.Radiobutton(ramka, text=znak, variable=operatsiia, value=znak).pack(side="left", padx=4)

rez = tk.StringVar(value="—")
rezultat = tk.Label(vikno, textvariable=rez, font=("Segoe UI", 16, "bold"))
rezultat.grid(row=4, column=0, columnspan=2, pady=6)


def porakhuvaty(podiia=None):
    try:
        a = float(pole_a.get().strip().replace(",", "."))
        b = float(pole_b.get().strip().replace(",", "."))
    except ValueError:
        rez.set("Помилка: введіть два числа")
        return

    znak = operatsiia.get()
    if znak == "+":
        znachennia = a + b
    elif znak == "−":
        znachennia = a - b
    elif znak == "×":
        znachennia = a * b
    elif znak == "÷":
        if b == 0:
            rez.set("Помилка: ділення на нуль")
            return
        znachennia = a / b
    else:
        rez.set("Помилка: невідома операція")
        return

    rez.set(f"Результат: {znachennia:g}")


def ochystyty(podiia=None):
    pole_a.delete(0, tk.END)
    pole_b.delete(0, tk.END)
    rez.set("—")


tk.Button(vikno, text="Порахувати", command=porakhuvaty).grid(
    row=3, column=0, columnspan=2, pady=4
)

pole_a.bind("<Return>", porakhuvaty)
pole_b.bind("<Return>", porakhuvaty)
vikno.bind("<Escape>", ochystyty)

vikno.mainloop()