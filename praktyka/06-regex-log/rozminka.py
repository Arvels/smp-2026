from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"

print("1.1. Рядки з words.txt великими літерами:")
with (DATA / "words.txt").open(encoding="utf-8") as f:
    for ryadok in f:
        print(ryadok.rstrip("\r\n").upper())

print("\n1.2. Середнє X-DSPAM-Confidence:")
suma = 0.0
kilkist = 0
with (DATA / "mbox-short.txt").open(encoding="utf-8") as f:
    for ryadok in f:
        if ryadok.startswith("X-DSPAM-Confidence:"):
            znachennia = float(ryadok.split(":", 1)[1].strip())
            suma += znachennia
            kilkist += 1

print(f"Кількість рядків: {kilkist}")
if kilkist:
    print(f"Середнє: {suma / kilkist:.9f}")
else:
    print("Середнє: неможливо обчислити — рядків не знайдено")