import tkinter as tk

#Define Window
root = tk.Tk()
root.title("Window Basics")
root.iconbitmap("hot_air_balloon.ico")
root.geometry("250x400")
root.resizable(0,1)
root.config(bg='blue')

#Second Window
top = tk.Toplevel(root)
top.title("Second Window")
top.config(bg="#123456")
top.geometry("200x200+0+50")


root.mainloop()