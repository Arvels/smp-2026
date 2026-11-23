-- Робота 8. SQL: обʼєднання і агрегація. База data/chinook.db
-- Під кожним рядком «-- N.» — ОДИН запит. Рядки з «--» — коментарі, їх можна дописувати.
-- Перевірка:  python praktyka/08-sql-join/perevir.py

-- 1. Треки гурту Queen: трек, альбом
SELECT t.Name, al.Title
FROM Track AS t
JOIN Album AS al ON t.AlbumId = al.AlbumId
JOIN Artist AS ar ON al.ArtistId = ar.ArtistId
WHERE ar.Name = 'Queen';

-- 2. Скільки треків у кожному жанрі: жанр, кількість; від найбільшого
SELECT g.Name, COUNT(*) AS TrackCount
FROM Track AS t
JOIN Genre AS g ON t.GenreId = g.GenreId
GROUP BY g.GenreId, g.Name
ORDER BY TrackCount DESC;

-- 3. Топ-10 клієнтів за сумою покупок: імʼя, прізвище, сума; від найбільшої
SELECT c.FirstName, c.LastName, ROUND(SUM(i.Total), 2) AS TotalSpent
FROM Customer AS c
JOIN Invoice AS i ON c.CustomerId = i.CustomerId
GROUP BY c.CustomerId
ORDER BY TotalSpent DESC
LIMIT 10;

-- 4. Виконавці, у яких більше 5 альбомів: виконавець, альбомів; від найбільшого
SELECT ar.Name, COUNT(al.AlbumId) AS AlbumCount
FROM Artist AS ar
JOIN Album AS al ON ar.ArtistId = al.ArtistId
GROUP BY ar.ArtistId
HAVING COUNT(al.AlbumId) > 5
ORDER BY AlbumCount DESC;

-- 5. Виконавці без жодного альбому
SELECT ar.Name
FROM Artist AS ar
LEFT JOIN Album AS al ON ar.ArtistId = al.ArtistId
WHERE al.AlbumId IS NULL;

-- 6. Середня тривалість треку по жанрах, у хвилинах з одним знаком: жанр, хвилин; від найдовшої
SELECT g.Name, ROUND(AVG(t.Milliseconds) / 60000.0, 1) AS AverageMinutes
FROM Genre AS g
JOIN Track AS t ON g.GenreId = t.GenreId
GROUP BY g.GenreId, g.Name
ORDER BY AverageMinutes DESC;

-- 7. Виторг за країнами (за рахунками): країна, сума; від найбільшого
SELECT BillingCountry, ROUND(SUM(Total), 2) AS Revenue
FROM Invoice
GROUP BY BillingCountry
ORDER BY Revenue DESC;

-- 8. Співробітники підтримки й скільки клієнтів у кожного: імʼя, прізвище, клієнтів; від найбільшого
SELECT e.FirstName, e.LastName, COUNT(c.CustomerId) AS CustomerCount
FROM Employee AS e
JOIN Customer AS c ON c.SupportRepId = e.EmployeeId
GROUP BY e.EmployeeId
ORDER BY CustomerCount DESC;