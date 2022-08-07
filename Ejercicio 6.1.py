class Vehiculo():
    Color = 'Rojo';
    Ruedas = 4;
    Puertas = 5;

class Coche(Vehiculo):
    Velocidad = 100;
    Cilindrada = 8;


d = Coche();
a = dir(d);
print(a);