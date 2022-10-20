import tkinter as tk
from PIL import Image, ImageTk

image = Image.open("ouvert.jpg")
image = image.resize((200, 150))
image2 = Image.open("ferme.jpg")
image2 = image2.resize((200, 150))
image3 = Image.open("soleil.png")
image3 = image3.resize((200, 150))
image4 = Image.open("soleil.png")
image4 = image4.resize((300, 200))

root = tk.Tk()
root.geometry("200x150")
root.maxsize(200, 150)
root.overrideredirect(True)
root.wm_attributes("-topmost", True)
root.wm_attributes("-transparent", True)

img = ImageTk.PhotoImage(image)
img2 = ImageTk.PhotoImage(image2)
img3 = ImageTk.PhotoImage(image3)
img4 = ImageTk.PhotoImage(image4)

label = tk.Label(root, image=img)
label.pack()


def ouvrir():
    global after1
    label.config(image=img)
    root.after_cancel(after2)
    root.after_cancel(after3)
    after1 = root.after(4000, fermer)


def fermer():
    label.config(image=img2)
    root.after(100, ouvrir)


def soleil():
    label.config(image=img3)
    root.after_cancel(after1)
    root.after(1000, grand_soleil)
    root.after(20000, ouvrir)
    root.after(int(1220000), soleil)


def resoleil():
    label.config(image=img3)
    after2


def grand_soleil():
    label.config(image=img4)
    after3


after2 = root.after(1000, grand_soleil)
after3 = root.after(500, resoleil)
ouvrir()
root.after(int(1200000/280), soleil)

root.mainloop()
