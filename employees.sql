CREATE DATABASE practice_db;
USE practice_db;


CREATE TABLE employees(
id INT PRIMARY KEY, name VARCHAR(50),
salary INT, dept VARCHAR(20)
);

INSERT INTO employees VALUES 
(1, 'Adam', 25000, 'HR'),
(2, 'Bob', 30000, 'IT'),
(3, 'Casey', 40000, 'IT'),
(4, 'David', 80000, 'HR'),
(5, 'Eva', 50000, 'Finance');

SELECT * FROM employees
WHERE dept = "HR";

SELECT dept, COUNT(name) FROM employees 
WHERE dept = "IT"
GROUP BY dept;

SELECT * FROM employees 
ORDER BY salary DESC LIMIT 1;

SELECT dept, AVG(salary) FROM  employees
GROUP BY dept;

SET SQL_SAFE_UPDATES = 0;
UPDATE employees
SET salary = salary + (salary * 10) / 100
WHERE dept = "IT";

DELETE FROM employees
WHERE salary > 30000;
