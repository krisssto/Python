from fileinput import close
import pickle

class Vehiculo:
    color = "Rojo"
    velocidades = 6
    puertas = 5

auto = Vehiculo

f = open('auto.txt', 'wb')
w = pickle.dump(auto, f)
f = close()

f = open('auto.txt', 'rb')
r = pickle.load(f)
f = close()

print (r.color)