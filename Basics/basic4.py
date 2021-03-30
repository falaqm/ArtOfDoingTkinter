import tkinter as tk

# Define Window
root = tk.Tk()
root.title("Window Basics")
root.iconbitmap("hot_air_balloon.ico")
root.geometry("500x400")
root.resizable(0, 0)


############
def make_label():
    """Print a label"""
    lb_output = tk.Label(output_frame, text=ent_text.get(), bg="#ff0000")
    lb_output.pack()
    ent_text.delete(0, tk.END)

def count_up(number):
    """Count Upp"""
    global value
    lbl_text = tk.Label(output_frame,text=number,bg="#ff0000")
    lbl_text.pack()
    value = number + 1

######
input_frame = tk.Frame(root, bg="#0000ff", width=500, height=100)
output_frame = tk.Frame(root, bg="#ff0000", width=500, height=400)
input_frame.pack(padx=10, pady=10)
output_frame.pack(padx=10, pady=(0, 10))
input_frame.grid_propagate(0)
output_frame.pack_propagate(0)

## add inputs

ent_text = tk.Entry(master=input_frame, width=40)
ent_text.grid(row=0, column=0, padx=5, pady=5)

btn_print = tk.Button(input_frame, text="Print", command=make_label)
btn_print.grid(row=0, column=1, padx=5, pady=5, ipadx=30)

# pass a parameter
value =5
btn_count = tk.Button(input_frame,text="count",command=lambda : count_up(value))
btn_count.grid(row=1,column=0,columnspan=2,padx=5,pady=5,sticky='we')
root.mainloop()
