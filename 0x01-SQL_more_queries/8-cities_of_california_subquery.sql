-- now seeming less likely
USE hbtn_0d_usa;
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;