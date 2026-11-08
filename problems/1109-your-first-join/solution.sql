-- Employee name + department name
SELECT e.name, d.name AS department
FROM employees e JOIN departments d on e.department_id=d.id; 
