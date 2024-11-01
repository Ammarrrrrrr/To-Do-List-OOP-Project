import sys
import os

def main_menu(tdlist):
    print("Hi, welcome to the to-do list application!")
    print("1. Add task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("0. Exit")
    
    try:
        selection = int(input("Select an option: "))

        if selection == 1:
            addToList(tdlist)
        elif selection == 2:
            RemoveFromList(tdlist)
        elif selection == 3:
            ShowAllListContents(tdlist)
        elif selection == 0:
            leave(tdlist)
        else:
            print("Invalid option. Please select a valid option.")
            newLine()
    except ValueError:
        print("Please enter a valid number.")
        newLine()

def addToList(tdlist):
    newLine()
    DataToAdd = input("Please enter your task: ")
    tdlist.append(DataToAdd)
    SaveToExternalFile(tdlist)
    print("Task added successfully.")
    newLine()

def RemoveFromList(tdlist):
    try:
        newLine()
        TaskNumberToRemove = int(input("Enter the number of the task to remove: "))
        if 1 <= TaskNumberToRemove <= len(tdlist):
            tdlist.pop(TaskNumberToRemove - 1) 
            SaveToExternalFile(tdlist)
            print("Task removed successfully.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Please enter a valid number.")
    newLine()

def ShowAllListContents(tdlist):
    newLine()
    if tdlist:
        print("Your Tasks:")
        for id, task in enumerate(tdlist, start=1): 
            print(f"{id}. {task}")
    else:
        print("No tasks available.")
    newLine()

def leave(tdlist):
    SaveToExternalFile(tdlist)
    newLine()
    print("Exiting the program. Goodbye!")
    sys.exit()

def LoadFile(tdlist):
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tdlist.extend(line.strip() for line in file)
    else:
        open("tasks.txt", "w").close()

def SaveToExternalFile(tdlist):
    with open("tasks.txt", "w") as file:
        for task in tdlist:
            file.write(task + "\n")

def newLine():
    print("\n")

def clearTerminal():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

listlol = []
LoadFile(listlol)
clearTerminal()

while True:
    main_menu(listlol)

