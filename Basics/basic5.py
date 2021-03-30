import tkinter as tk

#Define Window
root = tk.Tk()
root.title("Window Basics")
root.iconbitmap("hot_air_balloon.ico")
root.geometry("350x350")
root.resizable(0,0)

def make_label():
    """Print label"""
    num_label = tk.Label(output_frame,text=str(number.get()))
    num_label.pack()

#########################
input_frame = tk.LabelFrame(root,width=350,height=100,text="this is fun")
output_frame = tk.Frame(root,width=350,height=250)
input_frame.pack(padx=10,pady=10)
output_frame.pack(padx=10,pady=(0,10))

## Radio Buttons
number = tk.IntVar()
number.set(2)
radio_1 = tk.Radiobutton(input_frame,text="Print 1",variable=number,value=1)
radio_2 = tk.Radiobutton(input_frame,text="Print 2",variable=number,value=2)

btn_print = tk.Button(input_frame,text="print number",command=make_label)

radio_1.grid(row=0,column=0,padx=10,pady=10)
radio_2.grid(row=0,column=1,padx=10,pady=10)
btn_print.grid(row=1,column=0,columnspan=2,padx=10,pady=10)




root.mainloop()