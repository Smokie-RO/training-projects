import qrcode
import tkinter as tk
from tkinter import messagebox, filedialog

def generate_qr():
    data = text_input.get()
    if not data.strip():
        messagebox.showwarning("تحذير", "الرجاء إدخال رابط أو نص")
        return

    # اختيار مكان الحفظ
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if not save_path:
        return

    qr = qrcode.make(data)
    qr.save(save_path)
    messagebox.showinfo("تم", "✅ تم إنشاء رمز QR بنجاح")

# واجهة المستخدم
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x200")

tk.Label(root, text="أدخل النص أو الرابط:").pack(pady=10)

text_input = tk.Entry(root, width=50)
text_input.pack(pady=5)

tk.Button(root, text="Generate QR", command=generate_qr, bg="blue", fg="white", width=20).pack(pady=20)

root.mainloop()
