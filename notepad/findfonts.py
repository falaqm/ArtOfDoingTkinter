import tkinter
from tkinter import font
root = tkinter.Tk()
fonts = font.families()

for font in fonts:
    print(font)