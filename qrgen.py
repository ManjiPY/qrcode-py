import qrcode
import tkinter as tk
import socket
import os

from tkinter import filedialog

PC_NAME = socket.gethostname()

folder_name = "qrcode"

directory = (f"C:/Users/{PC_NAME}/Desktop/")

folder_path = os.path.join(directory, folder_name)

    
def generate_qr():
    url = entry.get()

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else: 
        print("Directory already exists.")

    if url:

        
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f"{folder_path}/qrcode.jpg")
        result_label.config(text="Your qrcode was generated: ")

def resize(window):
    windowheight = window.winfo_height()
    windowwidht = window.winfo_width()
    screenheight = window.winfo_screenheight()
    screenwidth = window.winfo_screenwidth()
    x = (screenwidth - windowwidht) //2
    y = (screenheight - windowheight) //2
    window.geometry(f"+{x}+{y}")

   

root = tk.Tk()
root.title("QR generator manjipy")
#root.geometry("800x400")
resize(root)


entry_label = tk.Label(root, text="Type your URL")
entry_label.pack(pady=(10, 5))
entry = tk.Entry(root, width=50)
entry.pack()


button = tk.Button(root, text="Generate", command=generate_qr)
button.config(bg="blue", fg="white", font=("Arial", 10, "bold"))
button.pack()   

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
