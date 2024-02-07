# Stenography : Hide Secret Messages Inside Images

# Pseudocode
# import necessary modules
import customtkinter
from tkinter import *
from tkinter import messagebox

# create log-in page

    # create window
root=Tk()
root.title("Log-in Page")
root.geometry("925x600")
root.configure(bg="#fff")
root.resizable(False, False)

img = PhotoImage(file="login.png")
Label(root, image=img, bg="white").place(x=50, y=50)
root.mainloop()



# Create the stenography using tkinter


