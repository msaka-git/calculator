from tkinter import *

def write(x):
    ind=len(input_area.get()) # The Entry widget is a standard Tkinter widget used to enter or display a single line of text. To fetch the current entry text, use the get method.

    input_area.insert(ind,str(x))

calcul = 5
n1 = 0

def operations_f(x):
    global calcul
    calcul=x
    global n1
    n1=float(input_area.get())
    input_area.delete(0,'end')

n2 = 0
def calculate():
    global n2
    n2=float(input_area.get())
    global calcul
    result=0
    if calcul==0: result=n1+n2
    elif calcul==1: result=n1-n2
    elif calcul==2: result=n1*n2
    elif calcul==3: result=n1 / n2

    input_area.delete(0,"end")
    input_area.insert(0,str(result))

def CE_f():
    input_area.delete(0,'end')


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

## Operation buttons
operations = []
for ops in range(0,4):
    operations.append(Button(font="Verdana 14 bold",width=2,command=lambda x=ops:operations_f(x)))

operations[0]['text'] = "+"
operations[1]['text'] = "-"
operations[2]['text'] = "*"
operations[3]['text'] = "/"


for i in range(0,4):
    operations[i].place(x=170,y=50+50*i)

zero_button=Button(text=0,font="Verdana 14 bold",command=lambda x=0:write(x))
zero_button.place(x=20,y=200)

point_button=Button(text=".",font="Verdana 14 bold",width=2,command=lambda x=".":write(x))
point_button.place(x=70,y=200)

equal_button=Button(text="=",fg="GREY",font="Verdana 14 bold",command=calculate)
equal_button.place(x=120,y=200)

ce_button=Button(text="CE", font="Verdana 14 bold",width=2,command=CE_f)
ce_button.place(x=20,y=250)

######### End operation buttons



window.mainloop()