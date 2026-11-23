import re
from collections import Counter
from pathlib import Path


SHABLON = re.compile(
    r'^(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\s+.*?'
    r'\[(?P<chas>[^\]]+)\]\s+'
    r'"(?P<metod>[A-Z]+)\s+(?P<shliakh>\S+)\s+HTTP/\d+(?:\.\d+)?"\s+'
    r'(?P<kod>\d{3})(?=\s|$)'
)


def main():
    zhurnal = Path(__file__).resolve().parents[2] / 'data' / 'access.log'
    ip_counter = Counter()
    kod_counter = Counter()
    pomylky_5xx = []
    rozibrano = 0
    propushcheno = 0

    with zhurnal.open(encoding='utf-8') as f:
        for ryadok in f:
            zbih = SHABLON.search(ryadok)
            if zbih is None:
                propushcheno += 1
                continue

            rozibrano += 1
            ip_counter[zbih['ip']] += 1
            kod_counter[zbih['kod']] += 1
            if zbih['kod'].startswith('5'):
                pomylky_5xx.append((zbih['chas'], zbih['shliakh']))

    print(f'Розібрано: {rozibrano}, пропущено: {propushcheno}')

    print('\nТоп-5 IP-адрес:')
    for ip, kilkist in ip_counter.most_common(5):
        print(f'  {ip}: {kilkist}')

    print('\nКоди відповіді:')
    for kod, kilkist in sorted(kod_counter.items()):
        print(f'  {kod}: {kilkist}')

    print(f'\nПомилки 5xx ({len(pomylky_5xx)} запити):')
    for chas, shliakh in pomylky_5xx:
        print(f'  {chas}  {shliakh}')


if __name__ == '__main__':
    main()