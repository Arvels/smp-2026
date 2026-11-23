"""Робота 10: форма реєстрації через PLACE.

Запуск:     python praktyka/10-maket/form_place.py
Перевірка:  python praktyka/10-maket/perevir.py
"""
import tkinter as tk

vikno = tk.Tk()
vikno.title("Реєстрація — place")
vikno.geometry("380x300")

# Що має бути у формі (README, крок 2):
#   заголовок «Реєстрація»;
#   чотири підписи з полями: Імʼя, Пошта, Телефон, Пароль — поле пароля з show="•";
#   прапорець «Погоджуюсь з умовами»;
#   кнопки «Зареєструватись» і «Скасувати» — внизу праворуч.
# Тут — ЛИШЕ place: x, y у пікселях (або relx, rely). Розмір вікна задайте явно, як нижче.

tk.Label(vikno, text="Реєстрація", font=("Arial", 16, "bold")).place(
    x=190, y=15, anchor="n"
)

for y, nazva in zip((70, 105, 140, 175), ("Імʼя", "Пошта", "Телефон", "Пароль")):
    tk.Label(vikno, text=f"{nazva}:").place(x=105, y=y, anchor="e")
    tk.Entry(vikno, show="•" if nazva == "Пароль" else "").place(
        x=120, y=y, width=245, anchor="w"
    )

tk.Checkbutton(vikno, text="Погоджуюсь з умовами").place(x=15, y=208)

tk.Button(vikno, text="Зареєструватись").place(x=270, y=252, anchor="ne")
tk.Button(vikno, text="Скасувати", command=vikno.destroy).place(
    x=365, y=252, anchor="ne"
)



vikno.mainloop()