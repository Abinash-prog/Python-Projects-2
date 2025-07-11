#  Load Existing items
# 1. create a new item
# 2. List item
# 3. mark item as complete
# 4. save item
import json

file_name = "todo_list.json"

def load_tasks():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return {"tasks":[]}

def save_taskes(tasks):
    try:
        with open(file_name, "w") as file:
            json.dump(tasks, file)
    except:
        print("failed to save")


def view_taskes(tasks):
    print()
    list_tasks = tasks['tasks']
    if len(list_tasks) == 0:
        print("No task to Display")
    else:
        print("Your To-Do List")
        for idx, task in enumerate(list_tasks):
            status = "[Completed]" if task['complete'] else "[Pending]"
            print(f"{idx + 1}. {task['description']} | {status}")

def create_task(tasks):
    description = input("Enter the task description: ").strip()
    if description:
        tasks['tasks'].append({'description': description, "complete":False})
        save_taskes(tasks)
        print("Task Added")
    else:
        print("Description cannot be empty")


def mark_task_complete(tasks):
    view_taskes(tasks)
    try:
        task_number = int(input("Enter the task number to mark as complete: ").strip())

        if 1<= task_number <= len(tasks):
            tasks['tasks'][task_number-1]['complete'] = True
            save_taskes(tasks)
            print("Task marked as complete")
        else:
            print("Invalid task number")
    except:
        print("Enter a valid number")


def main():
    tasks = load_tasks()
    # print(tasks)

    while True:
        print("\n To-DO List Manager")
        print("1. View Task")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_taskes(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please Try again.")


main()



