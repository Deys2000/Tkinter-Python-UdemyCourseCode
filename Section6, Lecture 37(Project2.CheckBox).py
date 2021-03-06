import tkinter as tk
from tkinter import ttk

window = tk
def clickme():
    button.configure(text="Hello " +name.get())
    button.grid(column=1, row=1)
def clickme():
    button.configure(text="Hello "+ name.get()+" "+numberChoose.get())

ttk.Label(text="choose a number:").grid(column=2, row=0)
number = tk.StringVar()
numberChoose = ttk.Combobox(width=12, textvariable=number)
numberChoose['values']=(1,2,4,50,100)
numberChoose.grid(column=1, row=1)
numberChoose.current(0)

ttk.Label(text="Enter a name:").grid(column=0, row=0)

name= tk.StringVar()
nameEntered = ttk.Entry(width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

button = ttk.Button(text="ClickMe", command=clickme)
button.grid(column=2, row=1)

chDisabled = tk.IntVar()
check1 = tk.Checkbutton(text="Disabled", variable=chDisabled, state="disabled")
check1.select()
check1.grid(column=0, row=4)

chChecked = tk.IntVar()
check2 = tk.Checkbutton(text="UnChecked", variable=chChecked)
check2.deselect()
check2.grid(column=1, row=4)

chEnabled = tk.IntVar()
check3 = tk.Checkbutton(text="Enabled", variable=chEnabled)
check3.select()
check3.grid(column=2, row=4)
window.mainloop()
