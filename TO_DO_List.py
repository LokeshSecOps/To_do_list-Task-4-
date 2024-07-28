import os

class TodoApp:
    def __init__(self):
        self.todos = []
    
    def add_task(self, task):
        self.todos.append({"task": task, "done": False})
        print(f"Added task: {task}")
    
    def list_tasks(self):
        if not self.todos:
            print("No tasks in the list.")
            return
        for i, todo in enumerate(self.todos, 1):
            status = "Done" if todo["done"] else "Pending"
            print(f"{i}. {todo['task']} - {status}")
    
    def mark_done(self, index):
        try:
            self.todos[index - 1]["done"] = True
            print(f"Marked task {index} as done.")
        except IndexError:
            print("Invalid task number.")
    
    def delete_task(self, index):
        try:
            removed_task = self.todos.pop(index - 1)
            print(f"Deleted task: {removed_task['task']}")
        except IndexError:
            print("Invalid task number.")
    
    def run(self):
        while True:
            print("\n1. Add Task\n2. List Tasks\n3. Mark Task Done\n4. Delete Task\n5. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                task = input("Enter the task: ")
                self.add_task(task)
            elif choice == "2":
                self.list_tasks()
            elif choice == "3":
                index = int(input("Enter task number to mark as done: "))
                self.mark_done(index)
            elif choice == "4":
                index = int(input("Enter task number to delete: "))
                self.delete_task(index)
            elif choice == "5":
                print("Exiting the app.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = TodoApp()
    app.run()
