-- lists all cities of California that can be found in database hbtn_0d_usa
SELECT id, name
FROM states
WHERE name = California
ORDER BY id ASC;
