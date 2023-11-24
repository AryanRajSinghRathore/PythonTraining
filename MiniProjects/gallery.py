import tkinter as tkr
from PIL import ImageTk, Image
import os
#from tkinter import *

counter = 0
def change():
    global counter
    img_label.config(image=img_array[counter%len(img_array)])
    counter +=1

    
app =tkr.Tk(__name__)
app.title('IMAGE VIEWER')
app.geometry('700x900')
app.configure(background='black')


##tkr.Label(app, text='WELCOME TO GALLERY' ,font=('Arial',20),fg='red').place(x=170,y=300)

files = os.listdir('wallpaper')
img_array=[]
for file in files:
    img =Image.open(os.path.join('wallpaper', file))
    resized_image = img.resize((400,400))                      
    img_array.append(ImageTk.PhotoImage(resized_image))

tkr.Label(app, image=img_array[0]).pack()
#img_label.pack()

##BUTTON
tkr.Button(app, text='NEXT', width=10,command=change, bg='white' , fg='black', font=(10)).place(x=270,y=420)




app.mainloop()

