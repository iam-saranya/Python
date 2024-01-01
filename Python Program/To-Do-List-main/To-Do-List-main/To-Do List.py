import json

def load_todo_list():
    try:
        with open('todo.json', 'r') as file:
            todo_list = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        todo_list = []
    return todo_list

def save_todo_list(todo_list):
    with open('todo.json', 'w') as file:
        json.dump(todo_list, file)

def display_todo_list(todo_list):
    print("\nTo-Do List:")
    for i, task in enumerate(todo_list, start=1):
        print(f"{i}. {task}")

def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Task '{task}' added.")

def mark_task_as_completed(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        completed_task = todo_list.pop(task_index - 1)
        print(f"Task '{completed_task}' marked as completed.")
    else:
        print("Invalid task index.")

def main():
    todo_list = load_todo_list()

    while True:
        print("\n1. View To-Do List")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Save and Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_todo_list(todo_list)
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(todo_list, task)
        elif choice == '3':
            task_index = int(input("Enter the task index to mark as completed: "))
            mark_task_as_completed(todo_list, task_index)
        elif choice == '4':
            save_todo_list(todo_list)
            print("To-Do List saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
