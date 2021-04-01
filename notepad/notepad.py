import tkinter as tk
from PIL import Image,ImageTk
from tkinter import scrolledtext,messagebox,filedialog

root = tk.Tk()
root.title("Notepad")
root.iconbitmap("Notepad.ico")
root.geometry("600x600")
root.resizable(0,0)

# define fonts and colors
text_color="#fffacd"
menu_color = "#dbd9db"
root_color="#6c809a"

root.config(bg=root_color)

# define functions
def change_font(event):
    """Change given font based on drop box"""
    if font_option.get()=="none":
        my_font =(font_family.get(),font_size.get())
    else:
        my_font= (font_family.get(),font_size.get(),font_option.get())

    # change the font style
    input_text.config(font=my_font)

def new_note():
    """Create a new note that clears the screen"""
    # use messagebox to ask for new note
    question = messagebox.askyesno("New Note","Are you sure to start a new note?")
    if question==1:
        input_text.delete("1.0",tk.END)

def close_note():
    """Closes note that quits program"""
    question = messagebox.askyesno("Close Note:","Are you sure?")
    if question==1:
        root.destroy()

def open_note():
    """Open Any previously saved note. First 3 lines store metadata"""
    open_name = filedialog.askopenfilename(title="Open File",
                                           initialdir="./",
                                           filetypes=[("Text File","*.txt"),("All Files","*.*")])
    with open(open_name,"r") as f:
        # Clear current text
        input_text.delete("1.0",tk.END)
        font_family.set(f.readline().strip())
        font_size.set(int(f.readline().strip()))
        font_option.set(f.readline().strip())

        # Change Font pass anything to change font
        change_font(1)
        text = f.read()

        input_text.insert("1.0",text)




def save_note():
    """Save the note. first 3 lines, font-family,font-size,font-option"""
    save_name = filedialog.asksaveasfilename(title="Save Note",defaultextension=".txt",
                                        initialdir="./",
                                        filetypes=[("Text File","*.txt"),("All Files","*.*")])
    with open(save_name,"w") as f:
        # first 3 lines are font-family font-size and font-option
        f.write(font_family.get()+"\n")
        f.write(str(font_size.get())+"\n")
        f.write(font_option.get()+"\n")
        # write the remaining body
        f.write(input_text.get("1.0",tk.END))

## define GUI layout
# define frames
menu_frame = tk.Frame(root,bg=menu_color)
text_frame = tk.Frame(root,bg=text_color)

menu_frame.pack(padx=5,pady=5)
text_frame.pack(padx=5,pady=5)

# menu frame
# menu: new,open,save,close,font-family,font-sizes,font-option

#buttons
new_image = ImageTk.PhotoImage(Image.open("new.png"))
new_button = tk.Button(menu_frame,image=new_image,bg=menu_color,command=new_note)

open_image = ImageTk.PhotoImage(Image.open("open.png"))
open_button = tk.Button(menu_frame,image=open_image,command=open_note)

save_image = ImageTk.PhotoImage(Image.open("save.png"))
save_button = tk.Button(menu_frame,image=save_image,command=save_note)

close_image = ImageTk.PhotoImage(Image.open("close.png"))
close_button = tk.Button(menu_frame,image=close_image,command=close_note)

# options
# font families
families= ["Terminal","Modern","Roman","Script","Courier","Arial","Calibri",
           "Cambria","Georgia","MS Gothic","SimSun","Tahoma",
           "Times New Roman","Verdana","Wingdings"]

font_family = tk.StringVar()
font_family.set("Terminal")
font_family_drop = tk.OptionMenu(menu_frame,font_family,*families,command=change_font)
font_family_drop.config(width=16) # set fit so width fits Times New Roman

# font sizes
sizes = [8, 10, 12, 14, 16, 20, 24, 32, 48, 64, 72, 96]
font_size = tk.IntVar()
font_size.set(12)
font_size_drop = tk.OptionMenu(menu_frame, font_size, *sizes,command=change_font)
font_size_drop.config(width=2) # set width to be constant

# font options
options =["none","bold","italic"]
font_option = tk.StringVar()
font_option.set("none")
font_option_drop = tk.OptionMenu(menu_frame,font_option,*options,command=change_font)
font_size_drop.config(width=15)

# placement
new_button.grid(row=0,column=0,padx=5,pady=5)
open_button.grid(row=0,column=1,padx=5,pady=5)
save_button.grid(row=0,column=2,padx=5,pady=5)
close_button.grid(row=0,column=3,padx=5,pady=5)
font_family_drop.grid(row=0,column=4,padx=5,pady=5)
font_size_drop.grid(row=0,column=5,padx=5,pady=5)
font_option_drop.grid(row=0,column=6,padx=5,pady=5)

# Text Frame
# Create the input text as scrolledtext widget.. so you can scroll through text field
# set default width and heiht more than the window size
my_font=(font_family.get(),font_size.get())
input_text = scrolledtext.ScrolledText(text_frame,bg=text_color,font=my_font,width=1000,height=100)
input_text.pack()

root.mainloop()

