import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Metric Helper")
root.iconbitmap("tool.ico")
# root.geometry("400x200")
root.resizable(0, 0)

# define fonts and colors
field_font = ("Cambria", 10)
bg_color = "#b15f05"
button_color = "#9a1913"
root.config(bg=bg_color)


# define functions

def convert():
    """Convert from one metric"""
    if ent_input_field.get()=="Enter Your Quantity" or not ent_input_field.get():
        return
    metric_values = {
        'femto': 10 ** -15,
        'pico': 10 ** -12,
        'nano': 10 ** -9,
        'micro': 10 ** -6,
        'milli': 10 ** -3,
        'centi': 10 ** -2,
        'deci': 10 ** -1,
        'base value': 10 ** 0,
        'deca': 10 ** 1,
        'hecto': 10 ** 2,
        'kilo': 10 ** 3,
        'mega': 10 ** 6,
        'giga': 10 ** 9,
        'tera': 10 ** 12,
        'peta': 10 ** 15

    }
    # get all user information
    start_value =float(ent_input_field.get())
    start_prefix = input_combobox.get()
    end_prefix = output_combobox.get()

    # convert to base unit
    base_value = start_value * metric_values[start_prefix]
    # convert to new metric value
    end_value = base_value/metric_values[end_prefix]
    
    ent_output_field.delete(0,tk.END)
    ent_output_field.insert(0,end_value)

def clear_all():
    ent_input_field.delete(0,tk.END)
    ent_output_field.delete(0,tk.END)

    ent_input_field.insert(0,"Enter Your Quantity")
    input_combobox.set('base value')
    output_combobox.set('base value')


# define widgets

ent_input_field = tk.Entry(master=root, width=22, font=field_font, borderwidth=3)
ent_output_field = tk.Entry(master=root, width=22, font=field_font, borderwidth=3)
lbl_equal_field = tk.Label(master=root, text="=", font=field_font, bg=bg_color)

ent_input_field.grid(row=0, column=0, padx=10, pady=10)
lbl_equal_field.grid(row=0, column=1, padx=10, pady=10)
ent_output_field.grid(row=0, column=2, padx=10, pady=10)

ent_input_field.insert(0, "Enter Your Quantity")

# dropdown

metric_list = ["femto", "pico", "nano", "micro", "milli",
               "centi", "deci", "base value", "deca", "hecto",
               "kilo", "mega", "giga", "tera", "peta"]

input_combobox = ttk.Combobox(root, value=metric_list, font=field_font, justify='center')
output_combobox = ttk.Combobox(root, value=metric_list, font=field_font, justify='center')
lbl_to = tk.Label(root, text="to", font=field_font, bg=bg_color)

input_combobox.grid(row=1, column=0, padx=10, pady=10)
lbl_to.grid(row=1, column=1, padx=10, pady=10)
output_combobox.grid(row=1, column=2, padx=10, pady=10)

input_combobox.set('base value')
output_combobox.set('base value')

'''
input_choice = tk.StringVar()
output_choice = tk.StringVar()
input_choice.set('base value')
output_choice.set('base value')

input_dropdown = tk.OptionMenu(root,input_choice,*metric_list)
output_dropdown = tk.OptionMenu(root,output_choice,*metric_list)
lbl_to =tk.Label(root,text="to",font=field_font,bg=bg_color)

input_dropdown.grid(row=1,column=0)
lbl_to.grid(row=1,column=1)
output_dropdown.grid(row=1,column=2)
'''

btn_convert = tk.Button(root, text="Convert", font=field_font, bg=button_color, activebackground=bg_color,
                        command=convert)
btn_convert.grid(row=2, column=0,  padx=10, pady=10, ipadx=50,sticky='we')

btn_clear = tk.Button(root,text="Clear all",font=field_font,bg=button_color,activebackground=bg_color,command=clear_all)
btn_clear.grid(row=2,column=2,padx=10,ipadx=50,sticky='we')
root.mainloop()
