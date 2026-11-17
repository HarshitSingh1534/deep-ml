-- your query
SELECT * from Employees e1 where e1.salary>(select avg(e2.salary) from employees e2 where e2.department=e1.department);
