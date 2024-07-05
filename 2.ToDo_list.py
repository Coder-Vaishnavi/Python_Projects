# Define an empty list to store tasks
todo_list = []

# Function to display the menu
def display_menu():
    print("Simple To-Do List")
    print("----------------------------")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Remove task")
    print("5. Exit")
    print()

# Function to add a task to the list
def add_task():
    task = input("Enter the task: ")
    todo_list.append({"task": task, "completed": False})
    print("Task added successfully!")

# Function to view all tasks
def view_tasks():
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for index, task in enumerate(todo_list, start=1):
            status = "✓" if task["completed"] else " "
            print(f"{index}. [{status}] {task['task']}")

# Function to mark a task as completed
def mark_completed():
    view_tasks()
    task_index = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= task_index < len(todo_list):
        todo_list[task_index]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

# Function to remove a task from the list
def remove_task():
    view_tasks()
    task_index = int(input("Enter task number to remove: ")) - 1
    if 0 <= task_index < len(todo_list):
        del todo_list[task_index]
        print("Task removed.")
    else:
        print("Invalid task number.")

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ").strip()
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
    
    input("Press Enter to continue...")
    print()