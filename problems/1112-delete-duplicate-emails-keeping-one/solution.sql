-- your query
SELECT id,email from person where id in (SELECT min(id) from person group by email);
