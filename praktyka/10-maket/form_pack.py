"""Робота 10: форма реєстрації через PACK.

Запуск:     python praktyka/10-maket/form_pack.py
Перевірка:  python praktyka/10-maket/perevir.py
"""
import tkinter as tk

vikno = tk.Tk()
vikno.title("Реєстрація — pack")

# Що має бути у формі (README, крок 2):
#   заголовок «Реєстрація»;
#   чотири підписи з полями: Імʼя, Пошта, Телефон, Пароль — поле пароля з show="•";
#   прапорець «Погоджуюсь з умовами»;
#   кнопки «Зареєструватись» і «Скасувати» — внизу праворуч.
# Тут — ЛИШЕ pack. Рядок «підпис + поле» зручно зробити окремою tk.Frame, усередині — теж pack.

tk.Label(vikno, text="Реєстрація", font=("Arial", 16, "bold")).pack(pady=(12, 10))

for nazva in ("Імʼя", "Пошта", "Телефон", "Пароль"):
    ryadok = tk.Frame(vikno)
    ryadok.pack(fill="x", padx=10, pady=3)

    tk.Label(ryadok, text=f"{nazva}:", width=10, anchor="e").pack(side="left")
    tk.Entry(ryadok, show="•" if nazva == "Пароль" else "").pack(
        side="left", fill="x", expand=True, padx=(6, 0)
    )

tk.Checkbutton(vikno, text="Погоджуюсь з умовами").pack(
    anchor="w", padx=15, pady=(8, 6)
)

knopky = tk.Frame(vikno)
knopky.pack(fill="x", padx=10, pady=(4, 12))
tk.Button(knopky, text="Скасувати", command=vikno.destroy).pack(side="right")
tk.Button(knopky, text="Зареєструватись").pack(side="right", padx=(0, 8))


vikno.mainloop()