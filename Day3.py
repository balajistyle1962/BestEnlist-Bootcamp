from tkinter import *
master = Tk()
var=IntVar()
master.title('Best Enlist Python Bootcamp 2021 Employees info')
master.geometry('400x300')
master.configure(background='grey')
Label(master,text='First Name').grid(row=0)
Label(master,text='Last Name').grid(row=2)
Label(master,text='E Id').grid(row=3)
e1=Entry(master)
e2=Entry(master)
e3=Entry(master)
e1.grid(row=0,column=1)
e2.grid(row=2,column=1)
e3.grid(row=3,column=1)
Label(master,text="Gender",justify=LEFT,padx=20).grid(row=4)
Radiobutton(master,text='male',padx=20,variable=var,value=1).grid(row=5)
Radiobutton(master,text='Female',padx=20,variable=var,value=2).grid(row=6)
Radiobutton(master,text='Others',padx=20,variable=var,value=3).grid(row=7)


Email = Label(master ,text = "Email Id").grid(row=8)
Mobile = Label(master,text = "Phone Number").grid(row=9)
e = Entry(master).grid(row=8,column=1)
m = Entry(master).grid(row=9,column=1)

def show():
    Label.config( text = clicked.get() )
    
Label(master,text="age").grid(row=10) 
options = [18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
clicked = IntVar()
drop = OptionMenu( master, clicked , *options )
drop.grid(row=10,column=1,sticky=W)

Label(master,text='Salary').grid(row=11)
e4=Entry(master)
e4.grid(row=11,column=1)

Label(master,text="No. of Experience").grid(row=12)
w = Spinbox(master, from_=0, to=20)
w.grid(row=12,column=1)
def callback():
    print("Welcom to Employee details")
b=Button(master,text="Submit").grid(row=13,column=1)



mainloop()
