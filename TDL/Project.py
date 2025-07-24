import tkinter as tk
from tkinter import messagebox
import os

TASK_FILE = "tasks.txt"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]
    return []

def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks(listbox.get(0, tk.END))
    else:
        messagebox.showwarning("تحذير", "يرجى إدخال مهمة!")

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
        save_tasks(listbox.get(0, tk.END))
    else:
        messagebox.showwarning("تحذير", "يرجى اختيار مهمة للحذف!")

# إعداد واجهة المستخدم
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# إدخال مهمة جديدة
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# زر إضافة
tk.Button(root, text="إضافة مهمة", command=add_task, bg="green", fg="white").pack()

# قائمة المهام
listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

# زر حذف
tk.Button(root, text="حذف المهمة المحددة", command=delete_task, bg="red", fg="white").pack()

# تحميل المهام المحفوظة
for task in load_tasks():
    listbox.insert(tk.END, task)

root.mainloop()
