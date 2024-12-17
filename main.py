import tkinter as tk
from tkinter import messagebox
import os

class ToDoListApp:

    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.configure(bg="#f5deb3")  # Set background to beige

        self.tdlist = []
        self.load_file()

        # Task Counter Section
        self.counter_frame = tk.Frame(root, bg="#f5deb3")
        self.counter_frame.pack(pady=10)

        self.total_tasks_label = tk.Label(
            self.counter_frame,
            text=f"Total Tasks: {len(self.tdlist)}",
            font=("Helvetica", 12, "bold"),
            fg="#8b4513",
            bg="#f5deb3",
        )
        self.total_tasks_label.pack(side=tk.LEFT, padx=10)

        self.done_tasks_label = tk.Label(
            self.counter_frame,
            text=f"Completed: {self.count_done_tasks()}",
            font=("Helvetica", 12, "bold"),
            fg="#8b4513",
            bg="#f5deb3",
        )
        self.done_tasks_label.pack(side=tk.LEFT, padx=10)

        # Title Label
        self.title_label = tk.Label(
            root,
            text="The To-Do List",
            font=("Brush Script MT", 30, "bold"),
            fg="#8b4513",  # Brownish color for text
            bg="#FAEBD7",
        )
        self.title_label.pack(pady=10)

        # Task Entry Section
        self.task_frame = tk.Frame(root, bg="#f5deb3")
        self.task_frame.pack(pady=5)

        self.task_label = tk.Label(
            self.task_frame,
            text="Enter the Task:",
            font=("Helvetica", 12, "bold"),
            fg="#8b4513",
            bg="#f5deb3",
        )
        self.task_label.pack(side=tk.LEFT, padx=5)

        self.task_entry = tk.Entry(self.task_frame, width=40, font=("Helvetica", 12))
        self.task_entry.pack(side=tk.LEFT, padx=5)

        self.add_button = tk.Button(
            self.task_frame,
            text="Add Task",
            command=self.add_task,
            bg="#3CB371",  # Light green 66bb6a
            font=("Helvetica", 10, "bold"),
        )
        self.add_button.pack(side=tk.LEFT, padx=5)

        # Task Listbox with Scrollbar
        self.listbox_frame = tk.Frame(root, bg="#f5deb3")
        self.listbox_frame.pack(pady=10)

        self.scrollbar = tk.Scrollbar(self.listbox_frame, orient=tk.VERTICAL)
        self.task_listbox = tk.Listbox(
            self.listbox_frame,
            width=50,
            height=15,
            font=("Helvetica", 12),
            yscrollcommand=self.scrollbar.set,
        )
        self.scrollbar.config(command=self.task_listbox.yview)

        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Load the list on start
        self.load_tasks()

        # Buttons Section with Two-Column Layout
        self.button_frame = tk.Frame(root, bg="#f5deb3")
        self.button_frame.pack(pady=10)

        # Edit Button (placed in column 0, row 0)
        self.edit_button = tk.Button(
            self.button_frame,
            text="Edit Task",
            command=self.edit_task,
            bg="#FF7F50",  # Light orange FF7F50
            font=("Helvetica", 10, "bold"),
        )
        self.edit_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        # Delete Button (placed in column 1, row 0)
        self.delete_button = tk.Button(
            self.button_frame,
            text="Delete Task",
            command=self.delete_task,
            bg="#ef5350",  # Light redef5350
            font=("Helvetica", 10, "bold"),
        )
        self.delete_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Done Button (placed in column 0, row 1)
        self.done_button = tk.Button(
            self.button_frame,
            text="Mark as Done",
            command=self.mark_done,
            bg="#4DB6AC",  # Soft teal
            font=("Helvetica", 10, "bold"),
        )
        self.done_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")


        # Search Button (placed in column 1, row 1)
        self.search_button = tk.Button(
            self.button_frame,
            text="Search Task",
            command=self.search_task,
            bg="#00BFFF",  # Light blue ADD8E6
            font=("Helvetica", 10, "bold"),
        )
        self.search_button.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Reset Button (placed in column 0, row 2)
        self.reset_button = tk.Button(
            self.button_frame,
            text="Back",
            command=self.load_tasks,
            bg="#78909c",  # Light grey
            font=("Helvetica", 10, "bold"),
        )
        self.reset_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        # Clear Button (placed in column 1, row 2)
        self.clear_button = tk.Button(
            self.button_frame,
            text="Clear All",
            command=self.clear_tasks,
            bg="#FFFACD",  # Light teal
            font=("Helvetica", 10, "bold"),
        )
        self.clear_button.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        # Exit Button (placed in column 0, row 3 spanning both columns)
        self.exit_button = tk.Button(
            self.button_frame,
            text="Exit",
            command=self.exit_app,
            bg="#e57373",  # Light red
            font=("Helvetica", 10, "bold"),
        )
        self.exit_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="ew")


    def load_file(self):
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r", encoding="utf-8") as file:
                self.tdlist = [line.strip() for line in file]
        else:
            open("tasks.txt", "w").close()

    def save_to_file(self):
        with open("tasks.txt", "w", encoding="utf-8") as file:
            for task in self.tdlist:
                file.write(task + "\n")

    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)  # Clear the listbox
        for index, task in enumerate(self.tdlist):
            self.task_listbox.insert(tk.END, task)  # Add task to the listbox
            if task.startswith("✔"):  # Check if the task is marked as done
                self.task_listbox.itemconfig(index, {'bg': 'lightgreen'})  # Highlight "done" tasks in green
        self.update_task_counters()



    def update_task_counters(self):
        self.total_tasks_label.config(text=f"Total Tasks: {len(self.tdlist)}")
        self.done_tasks_label.config(text=f"Completed: {self.count_done_tasks()}")

    def count_done_tasks(self):
        return sum(1 for task in self.tdlist if "✔" in task)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tdlist.append(task)
            self.save_to_file()
            self.load_tasks()
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
            self.load_tasks()
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
            self.load_tasks()
        except:
            messagebox.showwarning("Selection Error", "You must select a task to delete!")

    def mark_done(self):
        try:
            task_index = self.task_listbox.curselection()[0]  # Get the selected task index
            task = self.task_listbox.get(task_index)         # Get the selected task text

            if not task.startswith("✔"):  # Avoid adding the checkmark multiple times
                updated_task = f"✔ {task}"  # Add a checkmark to the task
                self.tdlist[task_index] = updated_task       # Update the task in the list
                self.save_to_file()                         # Save the updated list to the file
                self.load_tasks()                           # Reload the task list
            else:
                messagebox.showinfo("Info", "This task is already marked as done.")
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


    def clear_tasks(self):
        if messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?"):
            self.tdlist.clear()
            self.save_to_file()
            self.load_tasks()
            self.task_listbox.delete(0, tk.END)

    def exit_app(self):
        self.save_to_file()
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
    
