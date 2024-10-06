create database employee_sql;

use employee_sql;

# Creating Departments table for last part
CREATE TABLE departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    department_name VARCHAR(100)
);

INSERT INTO departments (department_name)
VALUES 
    ('Engineering'),
    ('Marketing'),
    ('Sales'),
    ('HR'),
    ('Finance');

#Part 1: DDL Statement for Creating the employees Table
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    salary DECIMAL(10, 2),
    hire_date DATE,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

#Part 2: SQL Queries

# 1. Insert several records into the employees table:

INSERT INTO employees (name, salary, hire_date, department_id) 
VALUES 
('John Doe', 55000.00, '2022-01-15', 1),
('Jane Smith', 45000.00, '2021-06-10', 2),
('Alice Johnson', 60000.00, '2020-09-20', 3),
('Bob Brown', 50000.00, '2019-12-01', 4),
('Charlie Black', 62000.00, '2023-02-28', 1),
('Eve White', 65000.00, '2021-11-05', 5),
('Frank Green', 70000.00, '2023-03-15', 1),
('Grace Blue', 62000.00, '2022-08-21', 3),
('Hank Orange', 47000.00, '2021-02-17', 2),
('Ivy Purple', 53000.00, '2020-05-10', 4);
       
# 2. Retrieve all employees in a specific department:

SELECT e.name, e.salary, d.department_name, e.hire_date
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE d.department_name = 'Engineering';

# 3. Update the salary of a specific employee:

UPDATE employees SET salary = 60000.00 WHERE name = 'Bob Brown';
SELECT * FROM employees;

# 4. Delete an employee record by ID:

DELETE FROM employees WHERE id = 2;
SELECT * FROM employees;

# 5. Retrieve the average salary of employees in each department:

SELECT d.department_name, AVG(e.salary) AS avg_salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_name;

# 6. Retrieve a list of all employees along with their department names from two tables (employees and departments):

SELECT e.name, d.department_name 
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id;
