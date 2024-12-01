import tkinter as tk
from tkinter import messagebox
import os

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

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tdlist:
        task_listbox.insert(tk.END, task)

def addToList():
    task = task_entry.get()
    if task:
        tdlist.append(task)
        SaveToExternalFile(tdlist)
        update_task_list()
        task_entry.delete(0, tk.END)

    else:
        messagebox.showwarning("Input Error", "You must enter a task!")


def editToList():

        try:
            selected_task_index = task_listbox.curselection()[0]
            ntask = task_entry.get()
            if ntask:
                task_listbox.delete(selected_task_index)
                update_task_list()
                tdlist[selected_task_index] = ntask
                SaveToExternalFile(tdlist)
            else:
                messagebox.showwarning("Value Error", "You must select a task to Edit!")

        except:
            messagebox.showwarning("Selection Error", "You must select a task to Edit!")


def deleteFromList():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        tdlist.pop(selected_task_index)
        SaveToExternalFile(tdlist)
           
    except:
        messagebox.showwarning("Selection Error", "You must select a task to delete!")
def mark_done():
    try:
        task_index = task_listbox.curselection()
        task = task_listbox.get(task_index)
        task_listbox.delete(task_index)
        task_listbox.insert(task_index, task + " - Done")
        task_listbox.itemconfig(task_index, {'bg': 'lightgreen'})  # Change background color to indicate completion
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done.")


def searchList():
    search_term = task_entry.get().lower()
    if search_term != "":
        task_listbox.delete(0, tk.END)
        for task in tdlist:
            if search_term in task.lower():
                task_listbox.insert(tk.END, task)
    else:
        messagebox.showwarning("Warning", "No tasks Available")

def Clear():
    task_listbox.delete(0, tk.END)


def Exit():
    SaveToExternalFile(tdlist)
    root.quit()





tdlist = []
LoadFile(tdlist)


root = tk.Tk()
root.title("To-Do List Application")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)


task_listbox = tk.Listbox(root, width=40, height=10, selectmode=tk.SINGLE)
task_listbox.pack(pady=10)

update_task_list()

add_button = tk.Button(root, text="Add Task", width=15, command=addToList)
add_button.pack(pady=5)

edit_button = tk.Button(root, text="Edit Task", width=15, command=editToList)
edit_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=15, command=deleteFromList)
delete_button.pack(pady=5)

search_button = tk.Button(root, text="Search Task", width=15, command=searchList)
search_button.pack(pady=5)

done_button = tk.Button(root, text="Mark as Done", width=15, command=mark_done)
done_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear Tasks", width=15, command=Clear)
clear_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", width=15, command=Exit)
exit_button.pack(pady=10)


root.mainloop()
