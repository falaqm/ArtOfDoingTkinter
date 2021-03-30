import tkinter as tk
from PIL import Image,ImageTk
import os
print(os.getcwd())

# Define Window
root = tk.Tk()
root.title("Window Basics")
root.iconbitmap("basics/hot_air_balloon.ico")
root.geometry("500x400")

def make_image():
    """Print image"""
    global cat_image
    cat_image = ImageTk.PhotoImage(Image.open("basics/cat.jpg"))
    cat_image_lbl = tk.Label(root,image=cat_image)
    cat_image_lbl.pack()


## PNG Image (not for JPEG)
my_image = tk.PhotoImage(file="basics/smallsmile.png", height=30)
lbl_image = tk.Label(root,image=my_image)
lbl_image.pack()

btn_image = tk.Button(root,image=my_image)
btn_image.pack()

## JPEG
# cat_image = ImageTk.PhotoImage(Image.open("cat.jpg"))
# cat_image_lbl = tk.Label(root,image=cat_image)
# cat_image_lbl.pack()

make_image()
root.mainloop()