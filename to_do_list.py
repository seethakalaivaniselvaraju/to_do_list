import os

tasks = []
if os.path.exists("tasks.txt"):
    with open("tasks.txt", "r") as file:
        for line in file:
            tasks.append(line.strip())
else:
    print("No saved tasks found. Starting with an empty list.")

def view():
    if not tasks:
        print("The list is empty. Choose 2 to add a task.")
    else:
        print("Current Task List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add():
    task = input("Enter your task: ")
    tasks.append(task)
    print("You have successfully entered the task.")
    with open("tasks.txt", "a") as file:
        file.write(f"{len(tasks)}. {task}\n")
    view()

def remove():
    if not tasks:
        print("No tasks to remove.")
    else:
        view()
        num=int(input("Enter the task number to delete:"))
        if num<=1 or num>=len(tasks):
            rt=tasks[num-1]
            tasks.pop(num)
        print(f"{rt} was removed succefully")
        


while True:
    try:
        Choice = int(input("\nEnter your choice:\n"
                           "1. View Task\n"
                           "2. Add Task\n"
                           "3. Remove Task\n"
                           "4. Exit\n"
                           "Your Choice: "))
        if Choice == 1:
            view()
        elif Choice == 2:
            add()
        elif Choice == 3:
            remove()
        elif Choice == 4:
            print("Saving and exiting. Goodbye!")
            break
        else:
            print("Please enter a valid option (1-4).")
    except ValueError:
        print("Please enter a number.")
