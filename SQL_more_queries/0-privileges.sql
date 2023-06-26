-- SHOW GRANTS PRACTICE
SELECT CONCAT('Grants for ', user, '@', host) AS 'Grants'
FROM mysql.user
WHERE user IN ('user_0d_1', 'user_0d_2')
  AND host = 'localhost';
