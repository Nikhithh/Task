def add_task(tasks, title):

    if title.strip() == "":
        return False

    task = {
        "title": title,
        "completed": False
    }

    tasks.append(task)

    return True
def view_tasks(tasks):

    if len(tasks) == 0:
        print("No tasks available.")
        return

    print("\n===== YOUR TASKS =====")

    for i, task in enumerate(tasks, start=1):

        if task["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        print(i, ".", task["title"], "-", status)
def complete_task(tasks, number):

    if number < 1 or number > len(tasks):
        return False

    tasks[number - 1]["completed"] = True

    return True
def delete_task(tasks, number):

    if number < 1 or number > len(tasks):
        return False

    deleted_task = tasks.pop(number - 1)

    print("Deleted task:", deleted_task["title"])

    return True

def edit_task(tasks, number ,new_title):

    if number < 1 or number > len(tasks):
        return False

    if new_title.strip() == "":
        return False

    tasks[number - 1]["title"] = new_title

    return True