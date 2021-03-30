import tkinter as tk

root = tk.Tk()
root.title("Checklist")
root.iconbitmap("Check.ico")
root.geometry("400x400")
root.resizable(0, 0)

# define fonts and color
my_font = ('Times New Roman', 12)
root_color = "#6c1cbc"  # "#8b24eb"
button_color = "#e2cff4"
root.config(bg=root_color)


## define functions
def add_item():
    """Add individual item in Listbox"""
    my_listbox.insert(tk.END, ent_list.get())
    ent_list.delete(0, tk.END)


def remove_item():
    """Remove selected(ANCHOR) item from the listbox"""
    my_listbox.delete(tk.ANCHOR)


def clear_list():
    """This will delete all items in listbox"""
    my_listbox.delete(0, tk.END)


def save_list():
    """Save the list to a simple text file"""
    with open("checklist.txt", "w") as f:
        # listbox.get returns tuple
        list_tuple = my_listbox.get(0, tk.END)
        for item in list_tuple:
            if item.endswith("\n"):
                f.write(item)
            else:
                f.write(item + '\n')


def open_list():
    """Open list upon starting program if there is one"""
    try:
        with open("checklist.txt", "r") as f:
            for line in f:
                my_listbox.insert(tk.END, line)
    except:
        return


## define layout
input_frame = tk.Frame(root, bg=root_color)
output_frame = tk.Frame(root, bg=root_color)
button_frame = tk.Frame(root, bg=root_color)

input_frame.pack()
output_frame.pack()
button_frame.pack()

## input frame layout
ent_list = tk.Entry(input_frame, width=35, borderwidth=3, font=my_font)
btn_add_list = tk.Button(input_frame, text="Add item", borderwidth=2, font=my_font, bg=button_color, command=add_item)

ent_list.grid(row=0, column=0, padx=5, pady=5)
btn_add_list.grid(row=0, column=1, padx=5, pady=5, ipadx=7)

## output frame layout
my_scrollbar = tk.Scrollbar(output_frame)

my_listbox = tk.Listbox(master=output_frame, height=15, width=45, borderwidth=3,
                        font=my_font, yscrollcommand=my_scrollbar.set)

my_listbox.grid(row=0, column=0)
my_scrollbar.grid(row=0, column=1, sticky='ns')

# link scrollbar to listbox
my_scrollbar.config(command=my_listbox.yview)

## button frame layout

btn_list_remove = tk.Button(master=button_frame, text="Remove item", borderwidth=2,
                            font=my_font, bg=button_color, command=remove_item)
btn_list_clear = tk.Button(button_frame, text="Clear List", borderwidth=2,
                           font=my_font, bg=button_color, command=clear_list)
btn_save = tk.Button(button_frame, text="Save List", borderwidth=2,
                     font=my_font, bg=button_color, command=save_list)
btn_quit = tk.Button(button_frame, text="Quit", borderwidth=2,
                     font=my_font, bg=button_color, command=root.destroy)

btn_list_remove.grid(row=0, column=0, padx=2, pady=10)
btn_list_clear.grid(row=0, column=1, padx=2, pady=10, ipadx=10)
btn_save.grid(row=0, column=2, padx=2, pady=10, ipadx=10)
btn_quit.grid(row=0, column=3, padx=2, pady=10, ipadx=27)

# open the previous list if available
open_list()

root.mainloop()
