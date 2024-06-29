import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime

DATA_FILE = 'unique_todo_data.json'

def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def refresh_tasks():
    """Refresh the list of tasks displayed."""
    for widget in task_frame.winfo_children():
        widget.destroy()
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        status = 'Done' if task['completed'] else 'Not Done'
        task_text = f"{task['title']} - {status} (Added: {task['date_added']})"
        lbl = tk.Label(task_frame, text=task_text)
        lbl.grid(row=i, column=0, sticky="w")
        btn_complete = tk.Button(task_frame, text="Complete", command=lambda i=i: complete_task(i))
        btn_complete.grid(row=i, column=1)
        btn_delete = tk.Button(task_frame, text="Delete", command=lambda i=i: delete_task(i))
        btn_delete.grid(row=i, column=2)

def add_task():
    """Add a new task."""
    title = entry_task.get()
    if title:
        tasks = load_tasks()
        new_task = {
            'title': title,
            'completed': False,
            'date_added': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        tasks.append(new_task)
        save_tasks(tasks)
        entry_task.delete(0, tk.END)
        refresh_tasks()
    else:
        messagebox.showwarning("Input Error", "Task title cannot be empty.")

def complete_task(index):
    """Mark a task as completed."""
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        save_tasks(tasks)
        refresh_tasks()
        check_all_tasks_completed()

def delete_task(index):
    """Delete a task."""
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        refresh_tasks()

def check_all_tasks_completed():
    """Check if all tasks are completed and notify the user."""
    tasks = load_tasks()
    if all(task['completed'] for task in tasks) and len(tasks) > 0:
        messagebox.showinfo("All Tasks Completed", "Great job! You have completed all tasks. Your chances for an extended internship with stipends are high!")

# Initialize the Tkinter application
app = tk.Tk()
app.title("To-Do List")

# Frame for task entry
frame = tk.Frame(app)
frame.pack(pady=10)

# Entry widget for task title
entry_task = tk.Entry(frame, width=50)
entry_task.pack(side=tk.LEFT, padx=10)

# Button to add task
btn_add = tk.Button(frame, text="Add Task", command=add_task)
btn_add.pack(side=tk.LEFT)

# Frame for displaying tasks
task_frame = tk.Frame(app)
task_frame.pack(pady=10)

# Load existing tasks
refresh_tasks()

# Start the Tkinter event loop
app.mainloop()
