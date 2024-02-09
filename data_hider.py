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
password = "highgradescutie"

# define functions:
    # a. show image():
        # i. prompt user to select an image file

def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title="Choose a file",
                                          filetypes=(("JPEG Files", "*.jpg"),
                                                     ("PNG Files", "*.png"),
                                                     ("All files", "*.*")))
    
        # ii. open the selected image and display it on a label widget                                               
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    label.configure(image=img, width=250, height=250)
    label.image = img

    # b. hide():
def Hide():
    global secret
    # i. check if the entered password is correct
    if check_password():
    # ii. if correct, get the secret message from the text input widget
        message = text1.get(1.0, END)   
    # ii. use LSB steganography to hide the message in the selected image
        secret = lsb.hide(str(filename), message)
     
     # iv. save the modified image as "newimage.png"
        save()
    else:
        messagebox.showwarning("Password Incorrect", "Please enter the correct password to hide data.")

    # c. Show():

def Show():
    # i. check if the entered password is correct
    if check_password():
    # ii. if correct, reveal the hidden message from the selected image using LSB steganography
        clear_message = lsb.reveal(filename)
        text1.delete(1.0, END)
        text1.insert(END, clear_message)
    else:
        messagebox.showwarning("Password Incorrect", "Please enter the correct password to reveal data.")
  
      
    # d. check_password():
def check_password():
     # i. prompt user to enter the password
    entered_password = filedialog.askstring("Password", "Enter Password:", show="*")
        # ii. check if the entered password matches the global password variable
    if entered_password == password:
        # iii. return True if matched, False otherwise
        return True
    else: 
        return False
    # e. save():
        # i. save the modified image as "newimage.png"
def save():
    secret.save("newimage.png")
    
# create gui components:
    # a. main icon and main title
icon_image = Image.open("logo.png")
image_icon = ImageTk.PhotoImage(icon_image)
root2.iconphoto(False, image_icon)

logo = PhotoImage(file="logo1.png")
Label(root2, image=logo, bg="#2f4155").place(x=10, y=0)
Label(root2, text="CYBER SCIENCE", bg="#2d4155", fg="white", font="arial 25 bold").place(x=100, y=20)

    # b. frames for displaying image and text input
# first frame
frame1 = Frame(root2, bd=3, bg="black", width=340, height=280, relief=GROOVE)
frame1.place(x=10, y=80)

label = Label(frame1, bg="black")
label.place(x=40, y=10)

# second frame
frame2 = Frame(root2, bd=3, width=340, height=280, bg="white", relief=GROOVE)
frame2.place(x=350, y=80)

text1 = Text(frame2, font="Roboto 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=320, height=295)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=320, y=0, height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

    # c. buttons for opening, saving, hiding and revealing data

# third frame
frame3 = Frame(root2, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame3.place(x=10, y=370)

Button(frame3, text="Open Image", width=10, height=2, font="arial 14 bold", command=showimage).place(x=20, y=30)
Button(frame3, text="Save Image", width=10, height=2, font="arial 14 bold", command=save).place(x=180, y=30)
Label(frame3, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

# fourth frame
frame4 = Frame(root2, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame4.place(x=360, y=370)

Button(frame4, text="Hide Data", width=10, height=2, font="arial 14 bold", command=Hide).place(x=20, y=30)
Button(frame4, text="Show Data", width=10, height=2, font="arial 14 bold", command=Show).place(x=180, y=30)
Label(frame4, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

# place gui components within the main window

# start the tkinter event loop
root2. mainloop()