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
root.geometry("975x600")
root.configure(bg="#fff")
root.resizable(False, False)

img = PhotoImage(file="login.png")
Label(root, image=img, bg="white").place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=600, y=100)

heading= Label(frame, text="Sign-in", fg= "#57a1f8", bg="white",font=("Microsoft Yahei UI Light",23, "bold"))
heading.place(x=100, y=5)

user = Entry (frame, width= 25, fg="black", border=0, bg="white",font=("Microsoft Yahei UI Light",11) )
user.place(x=30, y=80)
user.insert(0, "Username")

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)


code = Entry (frame, width= 25, fg="black", border=0, bg="white",font=("Microsoft Yahei UI Light",11) )
code.place(x=30, y=150)
code.insert(0, "Password")

Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)






root.mainloop()



# Create the stenography using tkinter


