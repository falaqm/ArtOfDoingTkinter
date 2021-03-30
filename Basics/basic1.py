# Labels and Pack

import tkinter as tk

# Define Window
root = tk.Tk()
root.title("Window Basics")
root.iconbitmap("hot_air_balloon.ico")
root.geometry("400x400")
root.resizable(0, 0)
root.config(bg='blue')

# Create Widgets
lbl_name_1 = tk.Label(root,text='Hello my name is Maria')
lbl_name_1.pack()

lbl_name_2 = tk.Label(root,text='Hello my name is Maria',font=('Arial',18,'bold'))
lbl_name_2.pack()


lbl_name_3 = tk.Label(root)
lbl_name_3.config(text="Hello my name is Maria")
lbl_name_3.config(font=('Cambria',10))
lbl_name_3.config(bg='#ff0077')
lbl_name_3.pack(padx=10,pady=50)


lbl_name_4 = tk.Label(root,text='Hello my name is Maria',bg="#000000",fg="green",)
lbl_name_4.pack(pady=(0,10),ipadx=50,ipady=10,anchor="w")


lbl_name_5 = tk.Label(root,text='Hello my name is Maria',bg="#ffffff",fg="#123456")
lbl_name_5.pack(fill=tk.BOTH,expand=True,padx=10,pady=10)

root.mainloop()
