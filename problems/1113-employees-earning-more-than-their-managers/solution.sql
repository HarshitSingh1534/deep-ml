-- your query
SELECT e1.name as name from employees e1 INNER JOIN employees e2 ON e1.manager_id=e2.id where e1.salary>e2.salary;
