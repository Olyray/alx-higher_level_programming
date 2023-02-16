-- Select cities from California
SELECT id, name FROM cities
    WHERE state_id = 1
    ORDER BY id ASC;
