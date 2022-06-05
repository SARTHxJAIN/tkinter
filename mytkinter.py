from tkinter import *
#import tkinter.messagebox

root = Tk()

#label = Label(root, text='Hi Sarthak').pack()

"""
topFrame = Frame(root).pack()
bottomFrame = Frame(root).pack(side=BOTTOM)
button1 = Button(topFrame, text="btn 1", fg="red").pack(side=LEFT)
button2 = Button(topFrame, text="btn 2", fg="blue").pack(side=LEFT)
button3 = Button(topFrame, text="btn 3", fg="green").pack(side=LEFT)
button4 = Button(bottomFrame, text="btn 4", fg="purple").pack(side=BOTTOM)
"""

"""
one = Label(root, text="One", background="red", foreground="white").pack()
two = Label(root, text="Two", background="green", foreground="black").pack(fill=X)
three = Label(root, text="Three", background="blue", foreground="white").pack(side=RIGHT, fill=Y)
"""

"""
label_1 = Label(root, text="name").grid(row=0, sticky=E)
label_2 = Label(root, text="password").grid(row=1, sticky=E)
entry_1 = Entry(root).grid(row=0, column=1)
entry_2 = Entry(root).grid(row=1, column=1)

c = Checkbutton(root, text="Keep me logged in").grid(columnspan=2)
"""

'''
def printName(event):
    print("Hello Sarthak")
btn1 = Button(root, text="Print",)
btn1.bind("<Button-1>", printName)
btn1.pack()
'''

"""
def left(event):
print('Left')
def middle(event):
print('Middle')
def right(event):
print('Right')

frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", left)
frame.bind("<Button-2>", middle)
frame.bind("<Button-3>", right)
frame.pack()
"""

"""
class tkbtn():
def __init__(self, master):
    frame = Frame(master).pack()

    self.printBtn = Button(frame, text="print msg", command=self.printMsg).pack(side=LEFT)
    self.quitBtn = Button(frame, text="Quit", command=frame.quit).pack(side=LEFT)

def printMsg(self):
    print('HI welcome to tkinter')

root = Tk()
b = tkbtn(root)
"""

'''
#-Menu
def doNothing():
    print('ok I wont...')

root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New", command=doNothing)
subMenu.add_command(label="Open", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Setting", command=doNothing)
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Undo", command=doNothing)
editMenu.add_command(label="Redo", command=doNothing)

#-Toolbar
toolbar = Frame(root, bg="blue")
insertbtn = Button(toolbar, text="Insert Image", command=doNothing).pack(side=LEFT, padx=2, pady=2)
printbtn =  Button(toolbar, text="Print", command=doNothing).pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

#-Status Bar
status = Label(root, text="Do nothing", bd=1, relief=SUNKEN, anchor=W).pack(side=BOTTOM, fill=X)
'''

'''
tkinter.messagebox.showinfo('Window Title', 'Hello Sarthak Welcome to kinter')

ans = tkinter.messagebox.askquestion('Question 1','Do you like Cars?')
if ans ==  'yes':
    print("Porche")
'''

'''
canvas = Canvas(root, width=200, height=100)
canvas.pack()

blackLine = canvas.create_line(0,0, 200,50)
redLine = canvas.create_line(0,100, 200,50, fill="red")
yellowBox = canvas.create_rectangle(25,25, 130,60, fill="yellow")

canvas.delete(redLine)
'''

'''
photo = PhotoImage(file="lion.png")
label = Label(root, image=photo)
label.pack()
'''

root.mainloop()

#if __name__ == '__main__':

