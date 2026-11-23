# Результат роботи 8: JOIN і GROUP BY

## 1. Вивід `python praktyka/08-sql-join/perevir.py`

```text
== 1. Треки гурту Queen: трек, альбом
     Name | Title
     A Kind Of Magic | Greatest Hits II
     Under Pressure | Greatest Hits II
     Radio GA GA | Greatest Hits II
     … ще 42
  ✅ правильно (рядків: 45)

== 2. Треків у кожному жанрі: жанр, кількість; від найбільшого
     Name | TrackCount
     Rock | 1297
     Latin | 579
     Metal | 374
     … ще 22
  ✅ правильно (рядків: 25)

== 3. Топ-10 клієнтів за сумою покупок: імʼя, прізвище, сума; від найбільшої
     FirstName | LastName | TotalSpent
     Helena | Holý | 49.62
     Richard | Cunningham | 47.62
     Luis | Rojas | 46.62
     … ще 7
  ✅ правильно (рядків: 10)

== 4. Виконавці з більш ніж 5 альбомами: виконавець, альбомів; від найбільшого
     Name | AlbumCount
     Iron Maiden | 21
     Led Zeppelin | 14
     Deep Purple | 11
     … ще 3
  ✅ правильно (рядків: 6)

== 5. Виконавці без жодного альбому
     Name
     Milton Nascimento & Bebeto
     Azymuth
     João Gilberto
     … ще 68
  ✅ правильно (рядків: 71)

== 6. Середня тривалість треку по жанрах, хв з одним знаком; від найдовшої
     Name | AverageMinutes
     Sci Fi & Fantasy | 48.5
     Science Fiction | 43.8
     Drama | 42.9
     … ще 22
  ✅ правильно (рядків: 25)

== 7. Виторг за країнами (за рахунками): країна, сума; від найбільшого
     BillingCountry | Revenue
     USA | 523.06
     Canada | 303.96
     France | 195.1
     … ще 21
  ✅ правильно (рядків: 24)

== 8. Співробітники підтримки й кількість їхніх клієнтів; від найбільшого
     FirstName | LastName | CustomerCount
     Jane | Peacock | 21
     Margaret | Park | 20
     Steve | Johnson | 18
  ✅ правильно (рядків: 3)

Разом: 8 з 8 пунктів ✅   (мінімум для зарахування — пункти 1–5)
```

## 2. Моє питання до бази

Який музичний жанр має найбільшу кількість проданих треків у магазині?

## 3. SQL-запит і перші рядки результату

```sql
SELECT
    g.Name AS Genre,
    SUM(il.Quantity) AS SoldTracks
FROM InvoiceLine AS il
JOIN Track AS t ON il.TrackId = t.TrackId
JOIN Genre AS g ON t.GenreId = g.GenreId
GROUP BY g.GenreId, g.Name
ORDER BY SoldTracks DESC, g.Name
LIMIT 5;
```

```text
Genre               | SoldTracks
--------------------|-----------
Rock                | 835
Latin               | 386
Metal               | 264
Alternative & Punk  | 244
Jazz                | 80
```

## 4. Відповідь керівнику магазину

Найбільший попит у магазині має жанр Rock — 835 проданих треків, що значно більше, ніж у Latin (386) та Metal (264).