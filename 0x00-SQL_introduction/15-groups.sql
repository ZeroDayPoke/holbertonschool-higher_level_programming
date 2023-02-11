-- find mode scr
SELECT score 'score', COUNT(score) 'number' FROM second_table GROUP BY score ORDER BY COUNT(score) DESC;
