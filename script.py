from tkinter import *

def write(x):
    print(x)

window=Tk()
window.geometry("250x300") # in pixels

input_area=Entry(font="Verdana 14 bold",width=15,justify=RIGHT)
input_area.place(x=20,y=20)

butons = []

for b in range(1,10):
    butons.append(Button(text=str(b),font="Verdana 14 bold",command=lambda x=b:write(x))) # Button settings from 1 to 9, command parameter is for=display the number clicked in input_area.


## MAtrix 3 x 3 to place buttons
counter=0
for m in range(0,3): # x axis
    for j in range(0,3): # y axis
        butons[counter].place(x=20+j*50,y=50+m*50)
        counter += 1






window.mainloop()