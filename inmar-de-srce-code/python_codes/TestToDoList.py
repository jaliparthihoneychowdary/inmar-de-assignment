
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
        # Create an instance of ToDoList before each test
        self.todo_list = ToDoList()

    def test_add_task(self):
        # Test adding a task
        self.todo_list.add_task("Task 1")
        self.assertIn("Task 1", self.todo_list.tasks)

    def test_remove_task(self):
        # Test removing an existing task
        self.todo_list.add_task("Task 2")
        self.todo_list.remove_task("Task 2")
        self.assertNotIn("Task 2", self.todo_list.tasks)

    def test_remove_nonexistent_task(self):
        # Test trying to remove a task that does not exist
        self.todo_list.add_task("Task 3")
        self.todo_list.remove_task("Task 4")  # Task 4 does not exist
        self.assertIn("Task 3", self.todo_list.tasks)  # Task 3 should still exist

    def test_get_tasks(self):
        # Test getting tasks
        self.todo_list.add_task("Task 5")
        self.todo_list.add_task("Task 6")
        self.assertEqual(self.todo_list.tasks, ["Task 5", "Task 6"])

    def test_complete_task(self):
        # Test completing a task
        self.todo_list.add_task("Task 7")
        self.todo_list.complete_task("Task 7")
        self.assertNotIn("Task 7", self.todo_list.tasks)

    def test_complete_nonexistent_task(self):
        # Test completing a task that does not exist
        self.todo_list.add_task("Task 8")
        self.todo_list.complete_task("Task 9")  # Task 9 does not exist
        self.assertIn("Task 8", self.todo_list.tasks)  # Task 8 should still exist

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)

