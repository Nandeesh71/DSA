# DBMS

-- Drop old table (optional if already created)
DROP TABLE IF EXISTS employees;

-- Create table
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department_id INT NOT NULL,
    salary DECIMAL(10,2) NOT NULL
);

-- Insert values (designed for all queries)
INSERT INTO employees (emp_id, name, department_id, salary) VALUES
-- Dept 10 (4 employees, range >20k, avg >50k)
(1, 'Alice', 10, 55000),
(2, 'Bob', 10, 72000),
(3, 'Charlie', 10, 48000),
(4, 'Diana', 10, 80000),

-- Dept 20 (5 employees, two >60k, total ~300k)
(5, 'Eve', 20, 65000),
(6, 'Frank', 20, 70000),
(7, 'George', 20, 62000),
(8, 'Hannah', 20, 60000),
(9, 'Ian', 20, 43000),

-- Dept 30 (3 employees, high salaries, avg > company avg)
(10, 'Jack', 30, 85000),
(11, 'Karen', 30, 90000),
(12, 'Leo', 30, 87000),

-- Dept 40 (3 employees, all salaries >=40k, low avg <60k, but one >70k)
(13, 'Mona', 40, 72000),
(14, 'Nick', 40, 45000),
(15, 'Olivia', 40, 41000),

-- Dept 50 (2 employees, no one below 40k, total salary between 80k–150k)
(16, 'Paul', 50, 42000),
(17, 'Quinn', 50, 46000);



Q1

Find the total salary paid per department, but only for departments where the total salary exceeds $100,000.

SELECT department_id, SUM(salary) AS total_salary 
FROM employees 
GROUP BY department_id 
HAVING SUM(salary) > 100000;

✅ Answer:

department_id | total_salary
--------------|-------------
10            | 255000
20            | 300000
30            | 262000
40            | 158000

(Dept 50 excluded since total = 88,000 < 100k)


---

🔹 Q2

List departments that have more than 3 employees and the average salary is greater than $50,000.

SELECT department_id, COUNT(*) AS employee_count, AVG(salary) AS avg_salary 
FROM employees 
GROUP BY department_id 
HAVING COUNT(*) > 3 AND AVG(salary) > 50000;

✅ Answer:

department_id | employee_count | avg_salary
--------------|----------------|-----------
10            | 4              | 63750.00
20            | 5              | 60000.00


---

🔹 Q3

Find departments where the difference between the highest and lowest salary is more than $20,000.

SELECT department_id, MAX(salary) - MIN(salary) AS salary_range 
FROM employees 
GROUP BY department_id 
HAVING MAX(salary) - MIN(salary) > 20000;

✅ Answer:

department_id | salary_range
--------------|-------------
10            | 32000
20            | 27000
40            | 31000


---

🔹 Q4

Find departments with at least 2 employees earning above $60,000.

SELECT department_id, COUNT(*) AS high_earners 
FROM employees 
WHERE salary > 60000 
GROUP BY department_id 
HAVING COUNT(*) >= 2;

✅ Answer:

department_id | high_earners
--------------|-------------
10            | 2
20            | 3
30            | 3


---

🔹 Q5

Find departments where the average salary is above the company-wide average salary.

SELECT department_id, AVG(salary) AS avg_salary 
FROM employees 
GROUP BY department_id 
HAVING AVG(salary) > (SELECT AVG(salary) FROM employees);

✅ Company-wide avg = 63000.

department_id | avg_salary
--------------|-----------
30            | 87333.33


---

🔹 Q6

Find departments where no employee earns below $40,000.

SELECT department_id 
FROM employees 
GROUP BY department_id 
HAVING MIN(salary) >= 40000;

✅ Answer:

department_id
-------------
10
20
30
40
50

(All depts satisfy since min ≥ 40k)


---

🔹 Q7

Find departments where the total salary expense is between $80,000 and $150,000.

SELECT department_id, SUM(salary) AS total_salary 
FROM employees 
GROUP BY department_id 
HAVING SUM(salary) BETWEEN 80000 AND 150000;

✅ Answer:

department_id | total_salary
--------------|-------------
50            | 88000


---

🔹 Q8

Find departments with exactly 3 employees.

SELECT department_id 
FROM employees 
GROUP BY department_id 
HAVING COUNT(*) = 3;

✅ Answer:

department_id
-------------
30
40


---

🔹 Q9

List departments where the average salary is higher than 1.2 times the minimum salary in that department.

SELECT department_id, AVG(salary) AS avg_salary, MIN(salary) AS min_salary 
FROM employees 
GROUP BY department_id 
HAVING AVG(salary) > 1.2 * MIN(salary);

✅ Answer:

department_id | avg_salary | min_salary
--------------|------------|-----------
10            | 63750.00   | 48000
20            | 60000.00   | 43000
30            | 87333.33   | 85000
40            | 52666.67   | 41000


---

🔹 Q10

Find departments that have at least one employee earning more than $70,000 but the average salary is below $60,000.

SELECT department_id, AVG(salary) AS avg_salary 
FROM employees 
GROUP BY department_id 
HAVING AVG(salary) < 60000 AND MAX(salary) > 70000;

✅ Answer:

department_id | avg_salary
--------------|-----------
40            | 52666.67


---

📘 SUBQUERY Questions


---

🔹 SQ1

Find employees who work in departments where the average salary is above $60,000.

SELECT name, department_id 
FROM employees 
WHERE department_id IN ( 
    SELECT department_id 
    FROM employees 
    GROUP BY department_id 
    HAVING AVG(salary) > 60000
);

✅ Answer:
(All employees in depts 10, 20, 30)

name    | department_id
--------|--------------
Alice   | 10
Bob     | 10
Charlie | 10
Diana   | 10
Eve     | 20
Frank   | 20
George  | 20
Hannah  | 20
Ian     | 20
Jack    | 30
Karen   | 30
Leo     | 30


---

🔹 SQ2

Find employees who earn more than the highest salary in department 20.

SELECT name, salary 
FROM employees 
WHERE salary > ( 
    SELECT MAX(salary) 
    FROM employees 
    WHERE department_id = 20
);

✅ Dept 20 max = 70,000.

name   | salary
-------|-------
Diana  | 80000
Jack   | 85000
Karen  | 90000
Leo    | 87000
Mona   | 72000


---

🔹 SQ3

Find employees whose salary is above the average salary of the department with the fewest employees.

SELECT name, salary, department_id 
FROM employees 
WHERE salary > ( 
    SELECT AVG(salary) 
    FROM employees 
    WHERE department_id = ( 
        SELECT department_id 
        FROM employees 
        GROUP BY department_id 
        ORDER BY COUNT(*) ASC 
        LIMIT 1 
    ) 
);

✅ Dept 50 has fewest (2 employees). Avg = (42k+46k)/2 = 44,000.

name    | salary | department_id
--------|--------|---------------
Alice   | 55000  | 10
Bob     | 72000  | 10
Charlie | 48000  | 10
Diana   | 80000  | 10
Eve     | 65000  | 20
Frank   | 70000  | 20
George  | 62000  | 20
Hannah  | 60000  | 20
Jack    | 85000  | 30
Karen   | 90000  | 30
Leo     | 87000  | 30
Mona    | 72000  | 40
Nick    | 45000  | 40
Olivia  | 41000  | 40
Quinn   | 46000  | 50


---

🔹 SQ4

Find employees who earn more than the average salary of employees who earn less than $50,000.

SELECT name, salary 
FROM employees 
WHERE salary > ( 
    SELECT AVG(salary) 
    FROM employees 
    WHERE salary < 50000
);

✅ Salaries <50k → {48k, 43k, 45k, 41k, 42k, 46k}. Avg = 44,166.

Employees > 44,166: everyone except Olivia (41k).

name    | salary
--------|-------
Alice   | 55000
Bob     | 72000
Charlie | 48000
Diana   | 80000
Eve     | 65000
Frank   | 70000
George  | 62000
Hannah  | 60000
Jack    | 85000
Karen   | 90000
Leo     | 87000
Mona    | 72000
Nick    | 45000
Paul    | 42000 ❌ (excluded)
Quinn   | 46000


