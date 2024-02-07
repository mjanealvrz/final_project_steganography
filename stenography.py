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

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=600, y=100)

heading= Label(frame, text="Sign-in", fg= "#57a1f8", bg="white",font=("Microsoft Yahei UI Light",23, "bold"))
heading.place(x=100, y=5)

user = Entry (frame, width= 25, fg="black", border=2, bg="white",font=("Microsoft Yahei UI Light",11) )
user.place(x=30, y=80)




root.mainloop()



# Create the stenography using tkinter


