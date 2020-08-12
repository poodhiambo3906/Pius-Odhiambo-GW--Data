/* Subquery to join the film and inventory TABLES in the rentals_db DATABASE*/

SELECT
	f.title, s."Number of Copies"
FROM
	film f,
	(SELECT	i.film_id, COUNT (i.film_id) AS "Number of Copies"
		FROM inventory i
		GROUP BY i.film_id
		HAVING COUNT (i.film_id) = 7
	) s
WHERE s.film_id = f.film_id
ORDER BY title
LIMIT 8

-- View: public.title_count

CREATE VIEW public.title_count
 AS
 SELECT f.title,
    s."Number of Copies"
   FROM film f,
    ( SELECT i.film_id,
            count(i.film_id) AS "Number of Copies"
           FROM inventory i
          GROUP BY i.film_id) s
  WHERE s.film_id = f.film_id;
  
-- Query to find the film title with 7 copies

SELECT title, "Number of Copies" FROM title_count
WHERE "Number of Copies" = 7;



