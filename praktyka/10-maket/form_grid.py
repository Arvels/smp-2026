"""Робота 10: форма реєстрації через GRID.

Запуск:     python praktyka/10-maket/form_grid.py
Перевірка:  python praktyka/10-maket/perevir.py
"""
import tkinter as tk

vikno = tk.Tk()
vikno.title("Реєстрація — grid")

# Що має бути у формі (README, крок 2):
#   заголовок «Реєстрація»;
#   чотири підписи з полями: Імʼя, Пошта, Телефон, Пароль — поле пароля з show="•";
#   прапорець «Погоджуюсь з умовами»;
#   кнопки «Зареєструватись» і «Скасувати» — внизу праворуч.
# Тут — grid для заголовка, підписів, полів і прапорця. Кнопки можна зібрати у tk.Frame (усередині — будь-який менеджер).

vikno.geometry("440x290")
vikno.columnconfigure(1, weight=1)

tk.Label(vikno, text="Реєстрація", font=("Arial", 17, "bold")).grid(
    row=0, column=0, columnspan=2, pady=(14, 12)
)

for riadok, nazva in enumerate(("Імʼя", "Пошта", "Телефон", "Пароль"), start=1):
    tk.Label(vikno, text=f"{nazva}:").grid(
        row=riadok, column=0, sticky="e", padx=(12, 6), pady=5
    )
    parametr = {"show": "•"} if nazva == "Пароль" else {}
    tk.Entry(vikno, **parametr).grid(
        row=riadok, column=1, sticky="ew", padx=(0, 12), pady=5
    )

zgoda = tk.BooleanVar(value=False)
tk.Checkbutton(vikno, text="Погоджуюсь з умовами", variable=zgoda).grid(
    row=5, column=0, columnspan=2, sticky="w", padx=12, pady=(8, 6)
)

knopky = tk.Frame(vikno)
knopky.grid(row=6, column=0, columnspan=2, sticky="e", padx=12, pady=8)
tk.Button(knopky, text="Скасувати", command=vikno.destroy).pack(side="right", padx=(6, 0))
tk.Button(knopky, text="Зареєструватись").pack(side="right")

vikno.mainloop()