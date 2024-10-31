import sys
import os

def main_menu(tdlist):
    print("Hi, welcome to the to-do list application!")
    print("1. Add task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("0. Exit")
    selection = int(input("Select option:"))
    
    if selection == 1:
        addToList(tdlist)
    elif selection == 2:
        RemoveFromList(tdlist)
    elif selection == 3:
        ShowAllListContents(tdlist)
    elif selection == 0:
        leave(tdlist)
    else:
        print("Invalid option")

def addToList(tdlist):
    DataToAdd = input("Please Enter Your Task: ")
    tdlist.append(DataToAdd)

def RemoveFromList(tdlist):
    try:
        TaskNumberToRemove = int(input("Enter the number of the task to remove: "))
        if 0 <= TaskNumberToRemove < len(tdlist):
            tdlist.pop(TaskNumberToRemove)
            print("Task removed successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def ShowAllListContents(tdlist):
    if tdlist:
        print("Your Tasks:")
        for id, task in enumerate(tdlist):
            print(id,".",task)
    else:
        print("No tasks available.")

def leave(tdlist):
    SaveToExternalFile(tdlist)
    sys.exit("Exiting the program. Goodbye!")

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

listlol = []
LoadFile(listlol)

while True:
    main_menu(listlol)
