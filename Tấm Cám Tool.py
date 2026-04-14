import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def process_logic(source_root):
    parent_dir = os.path.dirname(source_root)
    base_name = os.path.basename(source_root)
    
    pdf_root = os.path.join(parent_dir, f"{base_name} pdf")
    others_root = os.path.join(parent_dir, f"{base_name} Others")

    count_pdf = 0
    count_others = 0

    for root_dir, dirs, files in os.walk(source_root):
        for file in files:
            file_ext = os.path.splitext(file)[1].lower()
            target_base = pdf_root if file_ext == '.pdf' else others_root
            
            if file_ext == '.pdf': 
                count_pdf += 1
            else: 
                count_others += 1

            relative_path = os.path.relpath(root_dir, source_root)
            dest_dir = os.path.join(target_base, relative_path)
            
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            
            shutil.copy2(os.path.join(root_dir, file), os.path.join(dest_dir, file))
    
    messagebox.showinfo("Done!", f"Đã tách xong!\nPDF: {count_pdf}\nKhác: {count_others}")

def open_dialog():
    folder = filedialog.askdirectory(title="Chọn thư mục cần tách")
    if folder:
        process_logic(folder)

app = tk.Tk()
app.title("Tấm Cám Tool")
app.geometry("400x250")
app.eval('tk::PlaceWindow . center')

label_title = tk.Label(app, text="Vui lòng chọn thư mục cần tách", font=("Arial", 14, "bold"), fg="#2c3e50", pady=20)
label_title.pack()

btn_select = tk.Button(app, text="CHỌN THƯ MỤC", 
                       command=open_dialog, 
                       font=("Arial", 12, "bold"), 
                       bg="#3498db", fg="white", 
                       padx=20, pady=10, 
                       cursor="hand2")
btn_select.pack(pady=20)

app.mainloop()