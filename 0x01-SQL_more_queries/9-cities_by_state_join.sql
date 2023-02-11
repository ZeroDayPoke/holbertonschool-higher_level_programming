-- ASC ORD CITYID
SELECT cityid, city.name, stat.name
FROM cities AS city
    INNER JOIN states AS stat
    ON city.'state_id' = state.id
ORDER BY city.id ASC;
