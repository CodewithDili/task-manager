todo_list = []

def add_task(task):
    todo_list.append({"task": task, "completed": False})
    print(f"Task '{task}' added.")

def show_tasks():
    if not todo_list:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i}. {task['task']} - {status}")

def remove_task(task_number):
    try:
        removed_task = todo_list.pop(task_number - 1)
        print(f"Task '{removed_task['task']}' removed.")
    except IndexError:
        print("Invalid task number.")

def complete_task(task_number):
    try:
        todo_list[task_number - 1]["completed"] = True
        print(f"Task '{todo_list[task_number - 1]['task']}' marked as completed.")
    except IndexError:
        print("Invalid task number.")

while True:
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Remove Task")
    print("4. Complete Task")
    print("5. Exit")
    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        task_number = int(input("Enter the task number to remove: "))
        remove_task(task_number)
    elif choice == '4':
        task_number = int(input("Enter the task number to complete: "))
        complete_task(task_number)
    elif choice == '5':
        print("Exiting the to-do list application.")
        break
    else:
        print("Invalid input")
