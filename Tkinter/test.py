from tkinter import Tk,Label,Button,Entry

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height= 300)

my_label = Label(text="I am Label", font=("Arial",24,"bold"))
my_label.pack()

def button_clicked():
    my_label.config(text=input_entry.get())

my_but = Button(text="click me", command=button_clicked)

my_but.pack()


input_entry = Entry()
input_entry.pack()

window.mainloop()