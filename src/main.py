from services.task_service import (
    add_task,
    view_tasks,
    complete_task,
    delete_task,
    edit_task
)

from utils.logger import log

tasks = []
while True:

    print("\n===== TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Edit Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        title = input("Enter task title: ")

        if add_task(tasks, title):
            print("Task added successfully!")
            log("New task added")
        else:
            print("Task title cannot be empty.")


    elif choice == "2":

        view_tasks(tasks)

    
    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks available.")
            continue

        view_tasks(tasks)

        try:
            number = int(input("Enter task number: "))

            if complete_task(tasks, number):
                print("Task completed successfully!")
                log("Task marked as completed")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

   
    elif choice == "4":

        if len(tasks) == 0:
            print("No tasks available.")
            continue

        view_tasks(tasks)

        try:
            number = int(input("Enter task number to delete: "))

            if delete_task(tasks, number):
                print("Task deleted successfully!")
                log("Task deleted")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

  
    elif choice == "5":

        if len(tasks) == 0:
            print("No tasks available.")
            continue

        view_tasks(tasks)

        try:
            number = int(input("Enter task number to edit: "))
            new_title = input("Enter new task title: ")

            if edit_task(tasks, number, new_title):
                print("Task edited successfully!")
                log("Task edited")
            else:
                print("Invalid task number or empty title.")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "6":

        print("Thank you for using Task Manager!")
        break

    else:

        print("Invalid menu choice. Please try again.")