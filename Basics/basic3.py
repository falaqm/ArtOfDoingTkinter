import tkinter as tk

#Define Window
root = tk.Tk()
root.title("Windows Basic")
root.iconbitmap('task_icon.ico')
root.geometry("400x400")
root.resizable(1,0)

# lbl_name = tk.Label(root,text="Enter name")
# lbl_name.pack()
#
# btn_name= tk.Button(root,text="Submit your name")
# btn_name.grid(row=0,column=1)

# Define Frame

frame_pack_1 = tk.Frame(root,bg='red')
frame_grid_2 = tk.Frame(root, bg='blue')
frame_label_3 = tk.LabelFrame(root, text="grid system", borderwidth=5)

frame_pack_1.pack(fill=tk.BOTH,expand=True)
frame_grid_2.pack(fill=tk.X, expand=True)
frame_label_3.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

#frame 1

lbl_frame_grid_1 = tk.Label(frame_pack_1,text='text')
lbl_frame_grid_1.pack()
lbl_frame_grid_2 = tk.Label(frame_pack_1,text='text')
lbl_frame_grid_2.pack()
lbl_frame_grid_3 = tk.Label(frame_pack_1,text='text')
lbl_frame_grid_3.pack()

# frame 2
lbl_frame_grid_1 = tk.Label(frame_grid_2, text='text')
lbl_frame_grid_1.grid(row=0,column=0)
lbl_frame_grid_2 = tk.Label(frame_grid_2, text='text')
lbl_frame_grid_2.grid(row=1,column=1)
lbl_frame_grid_3 = tk.Label(frame_grid_2, text='text')
lbl_frame_grid_3.grid(row=2,column=2)


# frame 3
lbl_frame_grid_1 = tk.Label(frame_label_3, text='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
lbl_frame_grid_1.grid(row=0,column=0)
root.mainloop()