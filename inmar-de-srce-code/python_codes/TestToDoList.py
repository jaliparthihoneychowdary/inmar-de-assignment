
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed successfully.")
        else:
            print("Task not found in the list.")

    def get_tasks(self):
        if self.tasks:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No tasks found.")

    def complete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task completed successfully.")
        else:
            print("Task not found in the list.")

import unittest

class TestToDoList(unittest.TestCase):

    def setUp(self):
        self.todo_list = ToDoList()

    def test_add_task(self):
        self.todo_list.add_task("Task 1")
        self.assertIn("Task 1", self.todo_list.tasks)

    def test_remove_task(self):
        self.todo_list.add_task("Task 2")
        self.todo_list.remove_task("Task 2")
        self.assertNotIn("Task 2", self.todo_list.tasks)

    def test_remove_nonexistent_task(self):
        self.todo_list.add_task("Task 3")
        self.todo_list.remove_task("Task 4")  
        self.assertIn("Task 3", self.todo_list.tasks)

    def test_get_tasks(self):
        self.todo_list.add_task("Task 5")
        self.todo_list.add_task("Task 6")
        self.assertEqual(self.todo_list.tasks, ["Task 5", "Task 6"])

    def test_complete_task(self):
        self.todo_list.add_task("Task 7")
        self.todo_list.complete_task("Task 7")
        self.assertNotIn("Task 7", self.todo_list.tasks)

    def test_complete_nonexistent_task(self):
        self.todo_list.add_task("Task 8")
        self.todo_list.complete_task("Task 9") 
        self.assertIn("Task 8", self.todo_list.tasks) 

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)

