from tkinter import *

dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

root = Tk()
el = StringVar()

lista = Listbox(root)
lista.insert(END, *dias)
lista.pack()

label = Label(text="Dias")
label.pack()

root.mainloop()