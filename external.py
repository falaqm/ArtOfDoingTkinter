import tkinter as tk
from tkinter import ttk
import time
from tkinter import filedialog
import os

root = tk.Tk()
root.title("External")
root.geometry("400x200")
# def open_pgm():
#     my_pgm = filedialog.askopenfilename()
#     my_label.config(text=my_pgm)
#     os.system(my_pgm)
#
# my_button = tk.Button(root,text="Open Program",command=open_pgm)
# my_button.pack(pady=20)
#
# my_label= tk.Label(root,text="%%%")
# my_label.pack(pady=10)

progress = ttk.Progressbar(root,length=100,orient=tk.HORIZONTAL,mode="determinate")
def bar():
    progress["value"]=20
    root.update_idletasks()
    time.sleep(1)
    
    progress['value'] = 40
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 50
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 60
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 80
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 100
    
progress.pack(pady=10)

tk.Button(root, text = 'Start', command = bar).pack(pady = 10)

root.mainloop()
