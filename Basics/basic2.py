#buttons and grid
import tkinter as tk

#Define Window
root = tk.Tk()
root.title("Window Basics")
root.iconbitmap("hot_air_balloon.ico")
root.geometry("500x500+750+50")
root.resizable(0,0)


#Define Layout

btn_name = tk.Button(master=root,text="Name")
btn_name.grid(row=0,column=0)

btn_time = tk.Button(root,text="Time",bg="#00ffff")
btn_time.grid(row=0,column=1)

btn_place = tk.Button(root,text="Place",bg="#00ffff",activebackground="#ff0000")
btn_place.grid(row=0,column=2,padx=10,pady=10,ipadx=15)

btn_day = tk.Button(root,text="Day",bg="black",fg="white",borderwidth=5)
btn_day.grid(row=1,column=0,columnspan=3,sticky='we')

btn_test1 = tk.Button(root,text="test")
btn_test2 = tk.Button(root,text="test")
btn_test3 = tk.Button(root,text="test")
btn_test4 = tk.Button(root,text="test")
btn_test5 = tk.Button(root,text="test")
btn_test6 = tk.Button(root,text="test")

btn_test1.grid(row=2,column=0,padx=5,pady=5)
btn_test2.grid(row=2,column=1,padx=5,pady=5)
btn_test3.grid(row=2,column=2,padx=5,pady=5,sticky='w')
btn_test4.grid(row=3,column=0,padx=5,pady=5)
btn_test5.grid(row=3,column=1,padx=5,pady=5)
btn_test6.grid(row=3,column=2,padx=5,pady=5,sticky='w')

root.mainloop()