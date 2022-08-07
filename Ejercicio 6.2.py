class Alumno():
    def inicializar(self, nom, note):
        self.Nombre = nom;
        self.Nota = note;

    def mostrar(self):
        print (self.Nombre);
        print (self.Nota);

a = Alumno();
a.inicializar('Pepe', 7);
a.mostrar();