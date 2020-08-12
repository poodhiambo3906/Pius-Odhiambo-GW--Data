-- QUERY line (3-7) answers actors who appear in the film ALTER VICTORY in the `pagila` database

SELECT CONCAT(first_name,' ',s1.last_name) AS "Actors", title FROM film AS f,
(SELECT actor_id, film_id FROM public.film_actor fa
WHERE film_id = 18) AS s,
(SELECT first_name, last_name, actor_id FROM actor a) AS s1
WHERE s.actor_id = s1.actor_id AND f.film_id = s.film_id

 

-- inner Join query for Confirmation of subquery result above

SELECT CONCAT(first_name,' ', last_name) AS "Actors", f.title FROM actor a
JOIN film_actor AS fa
ON a.actor_id = fa.actor_id
JOIN film AS f
ON f.film_id = fa.film_id
WHERE title = 'ALTER VICTORY'


/* QUERY line(23-28) answers titles of films that the employee Jon Stephens rented to customers in the `pagila` database*/

SELECT CONCAT(st.first_name,' ',st.last_name) AS "Employee", f.title FROM staff AS st,
(SELECT staff_id,inventory_id FROM public.rental re
WHERE staff_id = 2) AS r,
(SELECT film_id, title FROM film ) AS f,
(SELECT inventory_id, film_id FROM inventory) AS i
WHERE st.staff_id = r.staff_id AND r.inventory_id = i.inventory_id AND i.film_id = f.film_id


-- inner Join query for Confirmation of subquery result above

SELECT CONCAT(first_name, ' ', last_name) Employee, f.title
FROM public.staff st
JOIN rental r
ON st.staff_id = r.staff_id
JOIN inventory i
ON r.inventory_id = i.inventory_id
JOIN film f
ON i.film_id = f.film_id
WHERE st.staff_id = 2
