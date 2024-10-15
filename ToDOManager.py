import os

# File to store tasks
TODO_FILE = "todo.txt"

# Function to read tasks from the file
def read_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

# Function to write tasks to the file
def write_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to display all tasks
def view_tasks():
    tasks = read_tasks()
    if tasks:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("\nNo tasks found.")

# Function to add a new task
def add_task():
    task = input("Enter the new task: ")
    tasks = read_tasks()
    tasks.append(task)
    write_tasks(tasks)
    print(f'Task "{task}" added successfully!')

# Function to remove a task by its number
def remove_task():
    view_tasks()
    tasks = read_tasks()
    if tasks:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            write_tasks(tasks)
            print(f'Task "{removed_task}" removed successfully!')
        else:
            print("Invalid task number.")
    else:
        print("No tasks to remove.")

# Main menu function
def main_menu():
    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Exiting the to-do list manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main_menu()
