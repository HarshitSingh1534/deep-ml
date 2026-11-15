-- your query
SELECT w.name,w.salary,t.title from workers w JOIN titles t ON w.title_id=t.title_id where w.salary=(SELECT MAX(salary) from workers) ORDER BY w.name;