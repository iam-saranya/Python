todo_list = []

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        task = input("Enter a new task: ")
        todo_list.append(task)
        print("Task added successfully!")
    elif choice == "2":
        print("\nTasks:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")
    elif choice == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
