class Alumno():
    def inicializar(self, nom, note):
        self.Nombre = nom;
        self.Nota = note;

    def mostrar(self):
        print (self.Nombre);
        print (self.Nota);
        if (self.Nota >= 7):
            print ('Aprobado!');

a = Alumno();
a.inicializar('Pepe', 7);
a.mostrar();