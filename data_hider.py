# Steganography  | Hide Secret Text Message Inside Image Using Python | GUI Tkinter Project
# Added functionality: Password Protection

# Pseudocode
# import necessary modules 
from tkinter import *
from tkinter import messagebox, filedialog
import os
from PIL import Image, ImageTk, ImageOps
from stegano import lsb


# create main window tkinter

    # a. set window title, size and background color
root2 = Tk()
root2.title("Steganography - Hide a Secret Text Message in an Image")
root2.geometry("700x540")
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

# Function to hide a file within an image
def hide_file():
    # Prompt the user to select the file to hide
    file_to_hide = filedialog.askopenfilename(title="Select File to Hide")
    if not file_to_hide:
        return  # User cancelled selection
    
    # Prompt the user to select an image to hide the file into
    image_to_hide_into = filedialog.askopenfilename(title="Select Image to Hide Into",
                                                    filetypes=(("Image Files", "*.png;*.jpg;*.jpeg"),))
    if not image_to_hide_into:
        return  # User cancelled selection
    
    # Specify the output path for the image with the hidden file
    output_image_path = "hidden_image.png"  # Modify as needed
    
    # Hide the file within the image using LSB steganography
    lsb.hide(image_to_hide_into, file_to_hide, output_image_path)
    
    messagebox.showinfo("File Hidden", "File hidden successfully.")

# Function to reveal and extract a hidden file from an image
def reveal_file():
    # Prompt the user to select the image containing the hidden file
    image_with_hidden_file = filedialog.askopenfilename(title="Select Image with Hidden File",
                                                        filetypes=(("Image Files", "*.png;*.jpg;*.jpeg"),))
    if not image_with_hidden_file:
        return  # User cancelled selection
    
    # Specify the output path for the extracted file
    output_file_path = "extracted_file"  # Modify as needed
    
    # Reveal and extract the hidden file from the image using LSB steganography
    lsb.reveal(image_with_hidden_file, output_file_path)
    
    messagebox.showinfo("File Extracted", "File extracted successfully.")

    
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

# Fourth frame for hiding and revealing data and files within the image
frame4 = Frame(root2, bd=3, bg="#2f4155", width=330, height=150, relief=GROOVE)
frame4.place(x=360, y=370)

# Button to hide text data
frame5 = Frame(root2, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame5.place(x=10, y=470)

hide_data_button = Button(frame5, text="Hide Data", width=10, height=2, font="arial 14 bold", command=Hide)
hide_data_button.place(x=20, y=30)

# Button to show text data
show_data_button = Button(frame5, text="Show Data", width=10, height=2, font="arial 14 bold", command=Show)
show_data_button.place(x=180, y=30)


# Fourth frame for hiding and revealing data and files within the image
# Button to hide file within image
hide_file_button = Button(frame4, text="Hide File within Image", command=hide_file, width=25)
hide_file_button.place(x=190, y=80)

# Button to reveal and extract file from image
reveal_file_button = Button(frame4, text="Reveal and Extract File from Image", command=reveal_file, width=30)
reveal_file_button.place(x=50, y=100)

# Label in frame4 indicating the purpose of the buttons
Label(frame4, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)


# start the tkinter event loop
root2. mainloop()
