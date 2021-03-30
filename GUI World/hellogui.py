import tkinter as tk
from PIL import Image,ImageTk

root = tk.Tk()
root.title("Hello GUI World!!")
root.iconbitmap("happy.ico")
root.geometry("400x400+250+50")
root.resizable(0,0)
root.config(bg="#224878")
# colors
input_color='#2a4494'
output_color ="#4ea5d9"

### Functions
def submit_name():
    """Say hello"""
    #create a label for user based on radio button values
    if case_style.get()=="normal":
        lbl_name = tk.Label(output_frame,text="Hello "+ent_name.get()+"!. Keep Learning",bg=output_color)
    elif case_style.get()=="upper":
        lbl_name = tk.Label(output_frame,text=("Hello "+ent_name.get()+"!. Keep Learning").upper(),bg=output_color)
    lbl_name.pack()
    
    ent_name.delete(0,tk.END)
    

### Create Frames

input_frame = tk.LabelFrame(root, bg=input_color)
output_frame = tk.LabelFrame(root, bg=output_color)
input_frame.pack(padx=10, pady=10)
output_frame.pack(padx=10, pady=(0, 10),fill=tk.BOTH,expand=True)

#input_frame.grid_propagate(0)

##### Create Widgets
#  input frame

ent_name = tk.Entry(input_frame,text="Enter your name",width=20)
ent_name.grid(row=0,column=0,padx=10,pady=10)

btn_submit = tk.Button(input_frame, text="Submit",command=submit_name)
btn_submit.grid(row=0,column=1,padx=10,pady=10,ipadx=20)

case_style =tk.StringVar()
case_style.set('normal')
rdbtn_normal = tk.Radiobutton(master=input_frame,text="Normal Case",variable=case_style,value='normal',bg=input_color,activebackground=input_color)
rdbtn_upper = tk.Radiobutton(master=input_frame,text="Upper Case",variable=case_style,value='upper',bg=input_color,activebackground=input_color)

rdbtn_normal.grid(row=1,column=0,padx=2,pady=2)
rdbtn_upper.grid(row=1,column=1,padx=2,pady=2)

# output frame
# my_img = ImageTk.PhotoImage(Image.open("smallsmile.png"))
my_img = tk.PhotoImage(file='smallsmile.png')
lbl_img = tk.Label(output_frame,image=my_img,bg=output_color)
lbl_img.pack(padx=5,pady=5)



root.mainloop()

