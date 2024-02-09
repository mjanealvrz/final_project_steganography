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
    # a. main logo and title
    # b. frames for displaying image and text input
    # c. buttons for opening, saving, hiding and revealing data
# place gui components within the main window
# start the tkinter event loop


