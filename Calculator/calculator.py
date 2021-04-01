import tkinter as tk

# define window
root = tk.Tk()
root.title("Calculator")
root.iconbitmap("Calculator.ico")
root.geometry("300x400")
root.resizable(0, 0)

# define colors and fonts
black_color = "#22190d"  # number button
orange_color = "#fc9404"  # command button
grey_color = "#c4c4ca"  # button
white_color = "#ffffff"  # entry
button_font = ("Arial", 18)
display_font = ("Arial", 30)


# define functions
def enable_buttons():
    """Enable all buttons and decimal on calculator"""
    btn_add.config(state=tk.NORMAL)
    btn_subtract.config(state=tk.NORMAL)
    btn_multiply.config(state=tk.NORMAL)
    btn_divide.config(state=tk.NORMAL)
    btn_exponent.config(state=tk.NORMAL)
    btn_inverse.config(state=tk.NORMAL)
    btn_square.config(state=tk.NORMAL)
    btn_decimal.config(state=tk.NORMAL)


def submit_number(number):
    """Add a number or decimal to display"""
    # insert number or decimal to the end of the display
    ent_display.insert(tk.END, number)
    # if decimal was pressed disable decimal so cant be pressed twice
    if "." in ent_display.get():
        btn_decimal.config(state=tk.DISABLED)


def operate(operator):
    """store 1st number of expression and operation to be used"""
    global first_number
    global operation

    # get the operator pressed and current displayed value
    operation = operator
    first_number = ent_display.get()

    # delete first number from display
    ent_display.delete(0, tk.END)
    # disable all operators till equal pressed
    btn_add.config(state=tk.DISABLED)
    btn_subtract.config(state=tk.DISABLED)
    btn_multiply.config(state=tk.DISABLED)
    btn_divide.config(state=tk.DISABLED)
    btn_exponent.config(state=tk.DISABLED)
    btn_inverse.config(state=tk.DISABLED)
    btn_square.config(state=tk.DISABLED)

    # enable decimal button
    btn_decimal.config(state=tk.NORMAL)


def equal():
    """Run the stored operation for fisrt and next number"""
    # perform desired operation
    if operation == "add":
        value = float(first_number) + float(ent_display.get())
    elif operation == "subtract":
        value = float(first_number) - float(ent_display.get())
    elif operation == "multiply":
        value = float(first_number) * float(ent_display.get())
    elif operation == "divide":
        if ent_display.get() == "0":
            value = "ERROR"
        else:
            value = float(first_number) / float(ent_display.get())
    elif operation == "exponent":
        value = float(first_number) ** float(ent_display.get())

    # Remove the current value and update with answer
    ent_display.delete(0, tk.END)
    ent_display.insert(0, value)
    # enable all operators and decimal
    enable_buttons()

def clear():
    """Clear Display"""
    ent_display.delete(0,tk.END)
    enable_buttons()

def inverse():
    """Calcualte inverse of number"""
    if ent_display.get()=="0":
        value="ERROR"
    else:
        value= 1/float(ent_display.get())

    #remove current value and update the value
    ent_display.delete(0,tk.END)
    ent_display.insert(0,value)

def square():
    """Calculate square of number"""
    value= float(ent_display.get())**2

    #remove current value and update the value
    ent_display.delete(0,tk.END)
    ent_display.insert(0,value)

def negate():
    """Negate a given number"""
    value = float(ent_display.get()) * -1
    #remove current value and update the value
    ent_display.delete(0,tk.END)
    ent_display.insert(0,value)

# Define GUI Layout
# define frames
display_frame = tk.LabelFrame(root)
button_frame = tk.LabelFrame(root)

display_frame.pack(padx=2, pady=(5, 20))
button_frame.pack(padx=2, pady=(0, 5))

# display frame
ent_display = tk.Entry(display_frame, width=50, font=display_font, bg=grey_color, borderwidth=5, justify="right")
ent_display.pack(padx=5, pady=5)

# button frame
btn_clear = tk.Button(button_frame, text="Clear", font=button_font, bg=orange_color, fg=black_color,command=clear)
btn_quit = tk.Button(button_frame, text="Quit", font=button_font, bg=orange_color, fg=black_color, command=root.destroy)
btn_inverse = tk.Button(button_frame, text="1/x", font=button_font, bg=orange_color, fg=black_color,command=inverse)
btn_square = tk.Button(button_frame, text="x^2", font=button_font, bg=orange_color, fg=black_color,command=square)
btn_exponent = tk.Button(button_frame, text="x^n", font=button_font, bg=orange_color, fg=black_color,
                         command=lambda: operate("exponent"))
btn_divide = tk.Button(button_frame, text=" / ", font=button_font, bg=orange_color, fg=black_color,
                       command=lambda: operate("divide"))
btn_multiply = tk.Button(button_frame, text="*", font=button_font, bg=orange_color, fg=black_color,
                         command=lambda: operate("multiply"))
btn_subtract = tk.Button(button_frame, text="-", font=button_font, bg=orange_color, fg=black_color,
                         command=lambda: operate("subtract"))
btn_add = tk.Button(button_frame, text="+", font=button_font, bg=orange_color, fg=black_color,
                    command=lambda: operate("add"))
btn_equal = tk.Button(button_frame, text="=", font=button_font, bg=orange_color, fg=black_color, command=equal)
btn_decimal = tk.Button(button_frame, text=".", font=button_font, bg=black_color, fg=white_color,
                        command=lambda: submit_number("."))
btn_negate = tk.Button(button_frame, text="+/-", font=button_font, bg=black_color, fg=white_color,command=negate)

btn_9 = tk.Button(button_frame, text="9", font=button_font, bg=black_color, fg=white_color,
                  command=lambda: submit_number(9))
btn_8 = tk.Button(button_frame, text="8", font=button_font, bg=black_color, fg=white_color,
                  command=lambda: submit_number(8))
btn_7 = tk.Button(button_frame, text="7", font=button_font, bg=black_color, fg=white_color,
                  command=lambda: submit_number(7))
btn_6 = tk.Button(button_frame, text="6", font=button_font, bg=black_color, fg=white_color,
                  command=lambda: submit_number(6))
btn_5 = tk.Button(button_frame, text="5", font=button_font, bg=black_color, fg=white_color,
                  command=lambda: submit_number(5))
btn_4 = tk.Button(button_frame, text="4", font=button_font, bg=black_color, fg=white_color,
                  command=lambda: submit_number(4))
btn_3 = tk.Button(button_frame, text="3", font=button_font, bg=black_color, fg=white_color,
                  command=lambda: submit_number(3))
btn_2 = tk.Button(button_frame, text="2", font=button_font, bg=black_color, fg=white_color,
                  command=lambda: submit_number(2))
btn_1 = tk.Button(button_frame, text="1", font=button_font, bg=black_color, fg=white_color,
                  command=lambda: submit_number(1))
btn_0 = tk.Button(button_frame, text="0", font=button_font, bg=black_color, fg=white_color,
                  command=lambda: submit_number(0))

# first row
btn_clear.grid(row=0, column=0, columnspan=2, pady=1, sticky='WE')
btn_quit.grid(row=0, column=2, columnspan=2, pady=1, sticky="WE")

# second row
btn_inverse.grid(row=1, column=0, pady=1, sticky="WE")
btn_square.grid(row=1, column=1, pady=1, sticky="WE")
btn_exponent.grid(row=1, column=2, pady=1, sticky="WE")
btn_divide.grid(row=1, column=3, pady=1, sticky="WE")
# third row
btn_7.grid(row=2, column=0, pady=1, sticky="WE", ipadx=20)
btn_8.grid(row=2, column=1, pady=1, sticky="WE", ipadx=20)
btn_9.grid(row=2, column=2, pady=1, sticky="WE", ipadx=20)
btn_multiply.grid(row=2, column=3, pady=1, sticky="WE", ipadx=20)
# fourth row
btn_4.grid(row=3, column=0, pady=1, sticky="WE")
btn_5.grid(row=3, column=1, pady=1, sticky="WE")
btn_6.grid(row=3, column=2, pady=1, sticky="WE")
btn_subtract.grid(row=3, column=3, pady=1, sticky="WE")
# fifth row
btn_1.grid(row=4, column=0, pady=1, sticky="WE")
btn_2.grid(row=4, column=1, pady=1, sticky="WE")
btn_3.grid(row=4, column=2, pady=1, sticky="WE")
btn_add.grid(row=4, column=3, pady=1, sticky="WE")
# sixth row
btn_negate.grid(row=5, column=0, pady=1, sticky="WE")
btn_0.grid(row=5, column=1, pady=1, sticky="WE")
btn_decimal.grid(row=5, column=2, pady=1, sticky="WE")
btn_equal.grid(row=5, column=3, pady=1, sticky="WE")

root.mainloop()
