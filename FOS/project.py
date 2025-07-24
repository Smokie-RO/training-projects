import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# التصنيفات
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Others': []
}

def organize_files(folder_path):
    if not folder_path:
        messagebox.showwarning("تحذير", "الرجاء اختيار مجلد أولاً")
        return

    for folder in file_types:
        os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in file_types.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(folder_path, folder, filename))
                    moved = True
                    break
            if not moved:
                shutil.move(file_path, os.path.join(folder_path, 'Others', filename))
    messagebox.showinfo("تم", "✅ تم ترتيب الملفات بنجاح")

# واجهة المستخدم
def browse_folder():
    folder = filedialog.askdirectory()
    folder_var.set(folder)

def start_organizing():
    folder_path = folder_var.get()
    organize_files(folder_path)

# إعداد نافذة tkinter
root = tk.Tk()
root.title("File Organizer")
root.geometry("400x200")

folder_var = tk.StringVar()

tk.Label(root, text="اختر المجلد لترتيب ملفاته:").pack(pady=10)
tk.Entry(root, textvariable=folder_var, width=40).pack()
tk.Button(root, text="Browse", command=browse_folder).pack(pady=5)
tk.Button(root, text="Start", command=start_organizing, bg="green", fg="white", width=20).pack(pady=20)

root.mainloop()
