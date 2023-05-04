from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)


#label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.pack()
my_label.config(padx=50, pady=50)

#Button
button = Button(text="Click me", command="button_clicked")
button.pack()

new_button = Button(text="New Button")
button.grid(column=3, row=0)


#Entry
input = Entry(width=10)
print(input.get())
input.pack()