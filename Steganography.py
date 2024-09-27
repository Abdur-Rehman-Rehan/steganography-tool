from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

# Initialize the root window
root = Tk()
root.title("Steganographic Forensic Tool")
root.geometry("700x500+250+180")
root.configure(bg="#2f4155")


# Function to open and display the selected image
def show_image():
    global filename, img
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select Image File",
        filetypes=(("PNG file", "*.png"), ("JPG File", "*.jpg"), ("All Files", "*.*")),
    )
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.config(image=img, width=250, height=250)
    lbl.image = img


# Function to hide the message inside the image
def hide_message():
    global secret
    message = text_box.get(1.0, END)
    secret = lsb.hide(str(filename), message)


# Function to reveal the hidden message from the image
def show_message():
    revealed_message = lsb.reveal(filename)
    text_box.delete(1.0, END)
    text_box.insert(END, revealed_message)


# Function to save the image with the hidden message
def save_image():
    try:
        if img is None:
            print("No image loaded")
            return
    except NameError:
        print("No image loaded")
        return

    options = {
        "title": "Save file as",
        "defaultextension": ".png",
        "filetypes": [("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg")],
    }

    file_path = filedialog.asksaveasfilename(**options)
    if file_path:
        if secret:
            secret.save(file_path)
            print(f"File saved as {file_path}")
        else:
            print("No hidden message to save")
    else:
        print("Operation failed or cancelled")


# Set the window icon and logo
image_icon = PhotoImage(file="logo.jpg")
root.iconphoto(False, image_icon)

logo = PhotoImage(file="logo.png")
Label(root, image=logo, bg="#2f4155").place(x=10, y=0)

Label(root, text="CYBER SCIENCE", bg="#2d4155", fg="white", font="arial 25 bold").place(
    x=100, y=20
)

# Frame to display the selected image
image_frame = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
image_frame.place(x=10, y=80)

lbl = Label(image_frame, bg="black")
lbl.place(x=40, y=10)

# Frame for the text box to display the hidden message
text_frame = Frame(root, bd=3, width=340, height=280, bg="white", relief=GROOVE)
text_frame.place(x=350, y=80)

text_box = Text(
    text_frame, font="Roboto 20", bg="white", fg="black", relief=GROOVE, wrap=WORD
)
text_box.place(x=0, y=0, width=320, height=295)

scrollbar = Scrollbar(text_frame)
scrollbar.place(x=320, y=0, height=300)
scrollbar.config(command=text_box.yview)
text_box.config(yscrollcommand=scrollbar.set)

# Frame for buttons to open and save the image
button_frame_1 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
button_frame_1.place(x=10, y=370)

Button(
    button_frame_1,
    text="Open Image",
    width=10,
    height=2,
    font="arial 14 bold",
    command=show_image,
).place(x=20, y=30)
Button(
    button_frame_1,
    text="Save Image",
    width=10,
    height=2,
    font="arial 14 bold",
    command=save_image,
).place(x=180, y=30)
Label(
    button_frame_1, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow"
).place(x=20, y=5)

# Frame for buttons to hide and reveal data
button_frame_2 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
button_frame_2.place(x=360, y=370)

Button(
    button_frame_2,
    text="Hide Data",
    width=10,
    height=2,
    font="arial 14 bold",
    command=hide_message,
).place(x=20, y=30)
Button(
    button_frame_2,
    text="Show Data",
    width=10,
    height=2,
    font="arial 14 bold",
    command=show_message,
).place(x=180, y=30)
Label(
    button_frame_2, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow"
).place(x=20, y=5)

# Run the Tkinter event loop
root.mainloop()
