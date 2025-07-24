import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import os

def merge_pdfs():
    files = filedialog.askopenfilenames(title="اختر ملفات PDF", filetypes=[("PDF files", "*.pdf")])
    if not files:
        return

    save_path = filedialog.asksaveasfilename(
        title="اختر مكان حفظ ملف الدمج",
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")]
    )
    if not save_path:
        return

    merger = PdfMerger()
    for pdf in files:
        merger.append(pdf)

    merger.write(save_path)
    merger.close()

    messagebox.showinfo("تم", f"✅ تم دمج الملفات بنجاح:\n{save_path}")

def split_pdf():
    file = filedialog.askopenfilename(title="اختر ملف PDF", filetypes=[("PDF files", "*.pdf")])
    if not file:
        return

    save_folder = filedialog.askdirectory(title="اختر مجلد لحفظ الصفحات")
    if not save_folder:
        return

    reader = PdfReader(file)
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        output_path = os.path.join(save_folder, f"page_{i+1}.pdf")
        with open(output_path, "wb") as f:
            writer.write(f)

    messagebox.showinfo("تم", f"✅ تم تقسيم الملف إلى الصفحات داخل:\n{save_folder}")

# واجهة المستخدم
root = tk.Tk()
root.title("PDF Merger / Splitter")
root.geometry("400x250")

tk.Label(root, text="PDF أدوات").pack(pady=15)

tk.Button(root, text="دمج ملفات PDF", command=merge_pdfs, bg="green", fg="white", width=30).pack(pady=10)
tk.Button(root, text="تقسيم ملف PDF", command=split_pdf, bg="orange", fg="black", width=30).pack(pady=10)

root.mainloop()
