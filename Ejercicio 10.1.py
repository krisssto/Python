from tkinter import *

def mostrarSeleccion():
   selection = "Seleccionaste la opcion " + str(var.get())
   label.config(text = selection)

def borrarForm():
    selection = "Borrando seleccion"
    var.set(None)
    label.config(text = selection)

root = Tk()
var = IntVar()
r1 = Radiobutton(root, text="Opcion 1", variable=var, value=1, command=mostrarSeleccion)
r1.pack(anchor = W)

r2 = Radiobutton(root, text="Opcion 2", variable=var, value=2, command=mostrarSeleccion)
r2.pack(anchor = W)

r3 = Radiobutton(root, text="Opcion 3", variable=var, value=3, command=mostrarSeleccion)
r3.pack(anchor = W)

r4 = Button(root, text="Reinicar", command=borrarForm)
r4.pack(anchor = W)

label = Label(root)
label.pack()

root.mainloop()