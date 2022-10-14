import tkinter as tk
from PIL import Image, ImageTk

image = Image.open("ouvert.jpg")
image = image.resize((200,150))
image2 = Image.open("ferme.jpg")
image2 = image2.resize((200,150))
image3 = Image.open("soleil.png")
image3 = image3.resize((200,150))

root = tk.Tk()
root.overrideredirect(True)
root.wm_attributes("-topmost", True)
root.wm_attributes("-transparent", True)
root.config(bg='systemTransparent')

img = ImageTk.PhotoImage(image)
img2 = ImageTk.PhotoImage(image2)
img3 = ImageTk.PhotoImage(image3)

label = tk.Label(root, image=img)
label.pack()

def ouvrir():
    global after1
    label.config(image=img)
    after1 = root.after(4000, fermer)

def fermer():
    label.config(image=img2)
    root.after(100, ouvrir)


def soleil():
    label.config(image=img3)
    root.after_cancel(after1)
    root.after(20000, ouvrir)
    root.after(1220000, soleil)

ouvrir()
root.after(1200000,soleil)

root.mainloop()