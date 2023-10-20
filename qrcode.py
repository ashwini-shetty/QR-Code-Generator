#!pip install qrcode[pil]
import qrcode
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

initial_window_width = 400
initial_window_height = 400
qr_img = None

def calculate_initial_window_size():
    url = url_entry.get()
    if url:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        return qr.make_image(fill_color="black", back_color="white").width, qr.make_image(fill_color="black", back_color="white").height
    return initial_window_width, initial_window_height

def generate_qr_code():
    global qr_img
    url = url_entry.get()
    if url:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        qr_img = qr.make_image(fill_color="black", back_color="white")
        img = ImageTk.PhotoImage(qr_img)
        qr_code_label.config(image=img)
        qr_code_label.image = img

        app.geometry(f"{initial_window_width}x{initial_window_height + 100}")  # Increase the window height
        clear_button.pack()
        app.update()  # Update the window to resize properly

def clear_qr_code():
    global qr_img
    url_entry.delete(0, "end")
    qr_code_label.config(image=None)
    qr_code_label.image = None
    app.geometry(f"{initial_window_width}x{initial_window_height + 100}")
    clear_button.pack_forget()
    
def save_qr_code():
    if qr_img:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            qr_img.save(file_path)

app = tk.Tk()
app.title("QR Code Generator")

url_label = tk.Label(app, text="Enter URL:")
url_label.pack()

url_entry = tk.Entry(app, width=40)
url_entry.pack()

generate_button = tk.Button(app, text="Generate QR Code", command=generate_qr_code, bg="green", fg="white")
generate_button.pack()

qr_code_label = tk.Label(app)
qr_code_label.pack()

save_button = tk.Button(app, text="Save QR Code", command=save_qr_code, bg="blue", fg="white")
save_button.pack()

# Add spacing between "Save QR Code" and "Clear" buttons
spacing_label = tk.Label(app, text="", width=5)
spacing_label.pack()

clear_button = tk.Button(app, text="Clear", command=clear_qr_code, bg="red", fg="white")
clear_button.pack()
clear_button.pack_forget()

initial_window_width, initial_window_height = calculate_initial_window_size()
app.geometry(f"{initial_window_width}x{initial_window_height + 100}")

app.mainloop()