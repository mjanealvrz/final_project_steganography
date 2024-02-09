# Steganography  | Hide Secret Text Message Inside Image Using Python | GUI Tkinter Project
# Added functionality: Password Protection

# Pseudocode
# import necessary modules 
from tkinter import *
from tkinter import messagebox, filedialog, simpledialog
import os
from PIL import Image, ImageTk
from stegano import lsb

# create main window tkinter

    # a. set window title, size and background color
root2 = Tk()
root2.title("Steganography - Hide a Secret Text Message in an Image")
root2.geometry("700x500")
root2.resizable(False, False)
root2.configure(bg="#2f4155")

# define global variables:
# define functions:
    # a. show image():
        # i. prompt user to select an image file
        # ii. open the selected image and display it on a label widget
    # b. hide():
        # i. check if the entered password is correct
        # ii. if correct, get the secret message from the text input widget
        # ii. use LSB steganography to hide the message in the selected image
        # iv. save the modified image as "newimage.png"
    # c. Show():
        # i. check if the entered password is correct
        # ii. if correct, reveal the hidden message from the selected image using LSB steganography
        # iii. display the revealed message in the text input widget
    # d. check_password():
        # i. prompt user to enter the password
        # ii. check if the entered password matches the global password variable
        # iii. return True if matched, False otherwise
    # e. save():
        # i. save the modified image as "newimage.png"

# create gui components:
    # a. main icon and main title
icon_image = Image.open("logo.png")
image_icon = ImageTk.PhotoImage(icon_image)
root2.iconphoto(False, image_icon)

logo = PhotoImage(file="logo1.png")
Label(root2, image=logo, bg="#2f4155").place(x=10, y=0)
Label(root2, text="CYBER SCIENCE", bg="#2d4155", fg="white", font="arial 25 bold").place(x=100, y=20)

    # b. frames for displaying image and text input
    # c. buttons for opening, saving, hiding and revealing data
# place gui components within the main window
# start the tkinter event loop


root2. mainloop()