import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime
import json
import os

TASKS_FILE = "tasks.json"

class Task:
    def __init__(self, title, due_date=None, priority="Medium", description="", completed=False):
        self.title = title
        self.due_date = due_date
        self.priority = priority
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {
            "title": self.title,
            "due_date": self.due_date,
            "priority": self.priority,
            "description": self.description,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            due_date=data.get("due_date"),
            priority=data.get("priority", "Medium"),
            description=data.get("description", ""),
            completed=data.get("completed", False)
        )

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=4)

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        data = json.load(f)
        return [Task.from_dict(d) for d in data]

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced To-Do List")
        self.tasks = load_tasks()

        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.refresh_list)

        tk.Entry(root, textvariable=self.search_var, width=50).pack(pady=5)

        self.listbox = tk.Listbox(root, width=100, height=20)
        self.listbox.pack()

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Add", command=self.add_task).grid(row=0, column=0)
        tk.Button(btn_frame, text="Edit", command=self.edit_task).grid(row=0, column=1)
        tk.Button(btn_frame, text="Mark Complete", command=self.mark_complete).grid(row=0, column=2)
        tk.Button(btn_frame, text="Delete", command=self.delete_task).grid(row=0, column=3)
        tk.Button(btn_frame, text="Save", command=self.save_all).grid(row=0, column=4)

        self.refresh_list()

    def refresh_list(self, *args):
        search_text = self.search_var.get().lower()
        self.listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            if search_text and search_text not in task.title.lower() and search_text not in task.description.lower():
                continue
            status = "✅" if task.completed else "❌"
            due = f" (Due: {task.due_date})" if task.due_date else ""
            priority = f"[{task.priority}]"
            display_text = f"{status} {task.title} {priority}{due}"

            if task.due_date and not task.completed:
                try:
                    due_date_obj = datetime.strptime(task.due_date, "%Y-%m-%d")
                    if due_date_obj < datetime.now():
                        display_text += " 🔥 Overdue!"
                except ValueError:
                    pass

            self.listbox.insert(tk.END, display_text)

    def add_task(self):
        title = simpledialog.askstring("Add Task", "Title:")
        if not title:
            return

        due_date = simpledialog.askstring("Add Task", "Due date (YYYY-MM-DD) (optional):")
        priority = simpledialog.askstring("Add Task", "Priority (High/Medium/Low):", initialvalue="Medium")
        description = simpledialog.askstring("Add Task", "Description:")

        new_task = Task(title, due_date, priority or "Medium", description or "", completed=False)
        self.tasks.append(new_task)
        self.refresh_list()

    def edit_task(self):
        index = self.listbox.curselection()
        if not index:
            return

        task = self.tasks[index[0]]

        new_title = simpledialog.askstring("Edit Task", "Title:", initialvalue=task.title)
        new_due = simpledialog.askstring("Edit Task", "Due date (YYYY-MM-DD):", initialvalue=task.due_date)
        new_priority = simpledialog.askstring("Edit Task", "Priority (High/Medium/Low):", initialvalue=task.priority)
        new_desc = simpledialog.askstring("Edit Task", "Description:", initialvalue=task.description)

        if new_title:
            task.title = new_title
        task.due_date = new_due
        task.priority = new_priority or "Medium"
        task.description = new_desc or ""

        self.refresh_list()

    def mark_complete(self):
        index = self.listbox.curselection()
        if not index:
            return
        task = self.tasks[index[0]]
        task.completed = True
        self.refresh_list()

    def delete_task(self):
        index = self.listbox.curselection()
        if not index:
            return
        confirm = messagebox.askyesno("Delete", "Are you sure you want to delete this task?")
        if confirm:
            self.tasks.pop(index[0])
            self.refresh_list()

    def save_all(self):
        save_tasks(self.tasks)
        messagebox.showinfo("Save", "Tasks saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
