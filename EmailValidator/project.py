import tkinter as tk
from tkinter import messagebox
import re


def validate_email():
    email = email_input.get().strip()

    # الشكل العام للبريد
    pattern = r"^[\w\.-]+@([\w\.-]+)\.\w+$"
    match = re.match(pattern, email)

    if not match:
        messagebox.showerror("النتيجة", "❌ البريد غير صحيح")
        return

    # التحقق من النطاق
    domain = email.split('@')[1].lower()
    allowed_domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]

    if domain in allowed_domains:
        messagebox.showinfo("النتيجة", f"✅ البريد صحيح ويستخدم نطاق معروف: {domain}")
    else:
        messagebox.showwarning("النتيجة", f"⚠️ البريد صحيح، لكن النطاق غير معتمد: {domain}")


# واجهة المستخدم
root = tk.Tk()
root.title("Email Validator")
root.geometry("400x200")

tk.Label(root, text="أدخل البريد الإلكتروني:").pack(pady=10)

email_input = tk.Entry(root, width=40)
email_input.pack()

tk.Button(root, text="تحقق", command=validate_email, bg="blue", fg="white", width=20).pack(pady=20)

root.mainloop()
