# RESTful сервис с использованием FastAPI и Redis

## Задание 1
Разработать RESTful сервис на FastAPI с использованием Redis.

## Задание 2
Перенос данных о статусе из таблицы short_names в таблицу full_names.

### Решение 1: Индексация столбцов name и запрос UPDATE
CREATE INDEX idx_short_names ON short_names (name);

CREATE INDEX idx_full_names ON full_names (name);

UPDATE full_names f 
SET status = COALESCE(s.status, f.status) 
FROM short_names s 
LEFT JOIN full_names f ON f.name = s.name 
WHERE f.status IS NULL;


### Решение 2: Создание временной таблицы
CREATE TEMPORARY TABLE temp_table ( 
    name TEXT, 
    status INTEGER 
);

COPY temp_table (name, status) 
FROM (
    SELECT s.name, s.status 
    FROM short_names s 
    JOIN full_names f ON f.name = s.name 
) WITH (FORMAT CSV, HEADER FALSE);

UPDATE full_names f 
SET status = t.status 
FROM temp_table t 
WHERE f.name = t.name;

DROP TABLE temp_table;