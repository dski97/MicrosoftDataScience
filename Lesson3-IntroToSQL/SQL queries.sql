-- SQLite
-- select all cities in the database
Select a.name as airport_name, c.city as city, c.country as country
from airports a, cities c
where a.city_id = c.id AND c.country = 'United Kingdom' AND c.city = 'London';
