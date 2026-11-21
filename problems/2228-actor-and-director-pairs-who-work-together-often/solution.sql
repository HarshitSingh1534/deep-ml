-- Frequent actor and director partnerships
SELECT p.name,ps.name,t.count from (
    SELECT fc.actor_id as actor_id,
    f.director_id as director_id,
    COUNT(DISTINCT(f.film_id)) as count
    from films f 
    JOIN film_cast fc ON f.film_id=fc.film_id 
    where fc.actor_id<>f.director_id 
    group by fc.actor_id,f.director_id 
    having COUNT(DISTINCT(f.film_id))>=3
) t 
JOIN people p ON t.actor_id=p.person_id 
JOIN people ps ON t.director_id=ps.person_id;