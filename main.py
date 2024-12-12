import tkinter as tk
from tkinter import messagebox
import os

class ToDoListApp:

    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tdlist = []  
        self.load_file()

        self.title_label = tk.Label(root, text="To-Do List Application", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.task_frame = tk.Frame(root)
        self.task_frame.pack(pady=10)
       
        self.task_entry = tk.Entry(self.task_frame, width=40, font=("Helvetica", 12))
        self.task_entry.pack(side=tk.LEFT, padx=5)

        self.add_button = tk.Button(self.task_frame, text="Add Task", command=self.add_task, bg="lightgreen")
        self.add_button.pack(side=tk.LEFT)

        self.listbox_frame = tk.Frame(root)
        self.listbox_frame.pack(pady=10)

        self.scrollbar = tk.Scrollbar(self.listbox_frame, orient=tk.VERTICAL)
        self.task_listbox = tk.Listbox(
            self.listbox_frame, 
            width=50, 
            height=15, 
            font=("Helvetica", 12), 
            yscrollcommand=self.scrollbar.set
        )
        self.scrollbar.config(command=self.task_listbox.yview)

        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task, bg="lightcoral")
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = tk.Button(self.button_frame, text="Clear All", command=self.clear_tasks, bg="lightblue")
        self.clear_button.pack(side=tk.LEFT, padx=5)

        self.edit_button = tk.Button(self.button_frame, text="Edit Task", command=self.edit_task, bg="lightyellow")
        self.edit_button.pack(side=tk.LEFT, padx=5)

        self.done_button = tk.Button(self.button_frame, text="Mark as Done", command=self.mark_done, bg="lightgreen")
        self.done_button.pack(side=tk.LEFT, padx=5)

        self.search_button = tk.Button(self.button_frame, text="Search Task", command=self.search_task, bg="lightblue")
        self.search_button.pack(side=tk.LEFT, padx=5)

        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.exit_app, bg="lightgray")
        self.exit_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = tk.Button(self.button_frame, text="Reset List", command=self.reset_list, bg="lightgray")
        self.reset_button.pack(side=tk.LEFT, padx=5)

    def load_file(self):
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                self.tdlist = [line.strip() for line in file]
        else:
            open("tasks.txt", "w").close()

    def save_to_file(self):
        with open("tasks.txt", "w") as file:
            for task in self.tdlist:
                file.write(task + "\n")

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tdlist.append(task)
            self.save_to_file()
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "You must enter a task!")

    def edit_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            # Populate the entry field with the selected task for editing
            selected_task = self.task_listbox.get(selected_task_index)
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(0, selected_task)

            # Modify the button behavior to confirm editing
            self.add_button.config(state=tk.DISABLED)
            self.edit_button.config(text="Confirm Edit", command=lambda: self.confirm_edit(selected_task_index))

        except IndexError:
            messagebox.showwarning("Selection Error", "You must select a task to edit!")

    def confirm_edit(self, index):
        """Confirm the edit and update the task."""
        new_task = self.task_entry.get().strip()
        if new_task:
            self.tdlist[index] = new_task  # Update the task in the list
            self.save_to_file()  # Save the updated list to the file
            self.task_listbox.delete(index)
            self.task_listbox.insert(index, new_task)
            self.task_entry.delete(0, tk.END)

            # Restore button behavior
            self.add_button.config(state=tk.NORMAL)
            self.edit_button.config(text="Edit Task", command=self.edit_task)
        else:
            messagebox.showwarning("Input Error", "You must enter a new task!")


    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
            self.tdlist.pop(selected_task_index)
            self.save_to_file()
        except:
            messagebox.showwarning("Selection Error", "You must select a task to delete!")

    def mark_done(self):
        try:
            task_index = self.task_listbox.curselection()
            task = self.task_listbox.get(task_index)
            self.task_listbox.delete(task_index)
            self.task_listbox.insert(task_index, task + " - Done")
            self.task_listbox.itemconfig(task_index, {'bg': 'lightgreen'}) 
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as done!")

    def search_task(self):
        search_term = self.task_entry.get().lower()
        if search_term != "":
            self.task_listbox.delete(0, tk.END)
            for task in self.tdlist:
                if search_term in task.lower():
                    self.task_listbox.insert(tk.END, task)
        else:
            messagebox.showwarning("Warning", "No tasks Available")


    def reset_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tdlist:
            self.task_listbox.insert(tk.END, task)


    def clear_tasks(self):
        if messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?"):
            self.tdlist.clear()
            self.save_to_file()
            self.task_listbox.delete(0, tk.END)

    def exit_app(self):
        self.save_to_file()
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
