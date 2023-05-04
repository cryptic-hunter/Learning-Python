import tkinter

window = tkinter.Tk() #equivalent to screens in turtle
window.title("My First GUI Program") #Adds a title on the window screen created by tkinter
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="This is the Label", font=("Arial", 24, "bold"))
my_label.pack()
# my_label.pack(side="left")

#change the properties of a label
my_label["text"] = "New Text"
my_label.config(text="New Text")


#Buttons

def button_clicked():
    print("I got clicked!")
    my_label["text"] = "Button got clicked"
    my_label.config(text="Button got clicked")

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()


#Entry

input = tkinter.Entry()
input.pack()
input.get()





window.mainloop() #keep the window on screen and don't let it close till the operation ends