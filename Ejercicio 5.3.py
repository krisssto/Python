def esBisiesto(numero):
    if numero % 4 == 0:
        print ("Es bisiesto")
        return False
    print ("No es bisiesto!")
    return True
    
numero = int(input("Ingrese el año que desea validar como bisiesto: "));
esBisiesto(numero)