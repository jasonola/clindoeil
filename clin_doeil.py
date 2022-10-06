# Import the required libraries
from tkinter import *
from PIL import ImageTk, Image
import threading

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the window
win.geometry("200x200")
# Image frame
frame = Frame(win, width=200, height=200)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# https://stackoverflow.com/questions/19080499/transparent-background-in-a-tkinter-window
# Hide the root window drag bar and close button
#win.overrideredirect(True)
# Make the root window always on top
win.wm_attributes("-topmost", True)
# Turn off the window shadow
win.wm_attributes("-transparent", True)
# Set the root window background color to a transparent color
win.config(bg='systemTransparent')

img = ImageTk.PhotoImage(Image.open("ouvert.jpg").resize((200,150)))

# Add a Label widget to add image
label = Label(frame, image = img)
label.pack()

# Run the window
win.mainloop()
