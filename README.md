# To-Do List Application

**Story:**  
Emma often forgets her tasks. She needs a simple, user-friendly application to manage her daily to-do list efficiently.

**Problem Statement:**  
Design a GUI-based to-do list application that enables users to add, edit, delete, search, and manage their tasks seamlessly while providing persistent data storage.

---
![image](https://github.com/user-attachments/assets/e3fec262-d144-4341-aa94-6dc2876db808)

https://github.com/user-attachments/assets/24b10148-c594-4ef4-98b1-8514b51928a8



## Features

### Task Management
- **Add Tasks**: Easily add tasks to your to-do list using a text input field.
- **Edit Tasks**: Modify existing tasks directly in the application.
- **Delete Tasks**: Remove tasks when completed or no longer needed.
- **Mark as Done**: Mark tasks as completed, with visual highlighting (green background).
- **Search Tasks**: Quickly find specific tasks by entering a search term.
- **Clear All Tasks**: Remove all tasks with a single click (confirmation required).

### Data Persistence
- **Save Tasks**: Automatically save tasks to a text file for future reference.
- **Load Tasks**: Load saved tasks upon application startup, including tasks marked as done.

### User-Friendly Interface
- Graphical user interface (GUI) built using Python's `tkinter`.
- Interactive buttons and listbox for seamless navigation and task management.

---

## How It Works

### Start-Up
- The application loads saved tasks from `tasks.txt`.
- Tasks marked as "done" are highlighted with a green background.

### Task Operations
1. **Adding a Task**:
   - Enter the task in the input field and click "Add Task."
2. **Editing a Task**:
   - Select a task from the list, click "Edit Task," make changes, and confirm.
3. **Marking as Done**:
   - Select a task and click "Mark as Done" to append " - Done" and highlight it.
4. **Deleting a Task**:
   - Select a task and click "Delete Task" to remove it.
5. **Clearing All Tasks**:
   - Click "Clear All" to remove all tasks after confirmation.
6. **Searching for Tasks**:
   - Enter a search term in the input field and click "Search Task" to filter matching tasks.

---

## Implementation Details

### Code Highlights
- The application uses Python's `tkinter` module for the GUI.
- Tasks are stored in memory (`self.tdlist`) and synced with `tasks.txt` for persistence.
- Tasks marked as "done" are visually distinguished in the listbox with a green background.

### Task List Persistence
- **Save to File**: The task list is saved to `tasks.txt` whenever a change is made.
- **Load from File**: Tasks, including their "done" status, are restored from `tasks.txt` when the application starts.

---

## Requirements

- **Python 3.x**
- No external libraries are needed (`tkinter` is included with Python).

---

## How to Run

1. Save the Python script to a file, e.g., `todo_app.py`.
2. Ensure `tasks.txt` exists in the same directory (an empty file will be created if missing).
3. Run the script:
   ```bash
   python main.py
4. Start managing your tasks with the intuitive GUI.
