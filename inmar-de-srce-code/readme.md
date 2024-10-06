 Question #1) Design a Simple Employee SQL Database Requirements:
1. Write the DDL statement that create a table named employees with the following columns:
○ id (integer, primary key, auto-increment)
○ name (string)
○ department (string)
○ salary (decimal)
○ hire_date (date)
2. Write
○ Insert several records into the employees table.
SQL queries to perform the following operations:
○ Retrieve all employees in a specific department.
○ Update the salary of a specific employee.
○ Delete an employee record by ID.
○ Retrieve the average salary of employees in each department.
○ Given two tables, employees and departments, where the departments table
contains information about department names and their IDs, write a query to retrieve a list of all employees along with their department names. If an employee does not belong to a department, their department name should show as NULL.


Question#2) Implement a Simple To-Do List Manager using Python Requirements:
1. Create a class ToDoList that supports the following operations:
○ add_task(task: str): Add a new task to the list.
○ remove_task(task: str): Remove a task from the list.
○ get_tasks(): Return a list of all tasks.
○ complete_task(task: str): Mark a task as completed.
2. Ensure that your implementation handles potential edge cases, such as:
○ Trying to remove a task that does not exist.
○ Trying to complete a task that does not exist.
3. Write unit tests to verify the functionality of your implementation.
v0.4

 Question #3) Implement a Simple Key-Value Store using Scala Requirements:
1. Create a class KeyValueStore that supports the following operations:
○ put(key: String, value: String): Add or update the value associated
with the key.
○ get(key: String): Option[String]: Retrieve the value associated with
the key, returning None if the key does not exist.
○ remove(key: String): Remove the key-value pair from the store.
○ keys(): List[String]: Return a list of all keys currently in the store.
2. Ensure that your implementation handles potential edge cases, such as:
○ Duplicate keys in put.
○ Trying to get or remove a key that doesn't exist.
3. Write unit tests to verify the functionality of your implementation.
v0.4
