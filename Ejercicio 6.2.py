class Alumno():
    def inicializar(self, nom, note):
        self.Nombre = nom;
        self.Nota = note;

    def mostrar(self):
        print (a.Nombre);
        print (a.Nota);

a = Alumno();
a.inicializar('Pepe', 7);
a.mostrar();