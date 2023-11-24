import tkinter as tkr
from tkinter import ttk
   
app =tkr.Tk(__name__)
app.title('IMAGE VIEWER')
app.geometry('700x900')
app.configure(background='black')
opt=tkr.Variable(app)
opt_values =('python','R','C','C#','JAVA')
#ttk.OptionMenu(app,opt,*opt_values).pack()
ttk.Combobox(app, textvariable = opt ,values=opt_values).pack()

#Radio box
rb_values= {'Python':1,'Machine Learning':2,'DL':3,'AI':4}

for k , v in rb_values.items():
    tkr.Radiobutton(app, text=k, variable=opt,values=v).pack()

app.mainloop()
