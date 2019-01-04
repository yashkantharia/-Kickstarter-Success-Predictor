import tkinter as tk

window = tk.Tk()
window.title("KICKSTARTER SUCCESS PREDICTOR")
window.geometry("400x250")



#------Calling Functions------------------
def suggestions():
    sugwindow = tk.Toplevel(window)
    sug = tk.Label(sugwindow,text="Suggestion.............................")
    sug.pack()

def disadv():
    diswindow = tk.Toplevel(window)
    dis = tk.Label(diswindow,text="Disadvantage...........................")
    dis.pack()



#~~~~~~~~~~~~~~~INPUTS~~~~~~~~~~~~~~~~~~~~~~~
#---LABELS--
lab1 = tk.Label(text="Category")
lab1.grid(column=0 , row=0, padx=5 )

lab2 = tk.Label(text="Goal (in USD)")
lab2.grid(column=4 , row=0, padx=5 )

lab3 = tk.Label(text="Duration (in days)")
lab3.grid(column=8 , row=0, padx=5 )

#--------INPUT FIELDS-------
#---DROPDOWN----
variable = tk.StringVar(window)
variable.set("Gaming") # default value

d1 = tk.OptionMenu(window, variable, "Gaming", "Technology", "Music", "Other")
d1.grid(column=0, row=1, padx=5)

#Textboxes
tb2 = tk.Text(window, height=2 ,width=10)
tb2.grid(column=4, row=1, padx=5)

tb3 = tk.Text(window, height=2 ,width=10)
tb3.grid(column=8, row=1, padx=5)


#------BUTTON------
but1 = tk.Button(text="Submit")
but1.grid(column=4, row= 3, pady=5)

#~~~~~~~~~~~~~~~~Output~~~~~~~~~~~~~~~~~~~~~

lab4 = tk.Label(text="Prediction:")
lab4.grid(column=0 , row=10, pady=5 )

tb1 = tk.Text(window, height=2 ,width=10)
tb1.grid(column=4, row=10, pady=5)

#----Advanced Output Buttons---
but2 = tk.Button(text="Disadvantages", command = disadv)
but2.grid(column=4, row=12 , pady=5)

but3 = tk.Button(text="Suggestions", command = suggestions)
but3.grid(column=4, row=15 , pady=5)




window.mainloop()

