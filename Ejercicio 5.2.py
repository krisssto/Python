def esPrimo(numero):
    for n in range(2, numero)    :
        if numero % n == 0:
            print ("No es primo")
            return False
    print ("Es primo!")
    return True
    
    
numero = int(input("Ingrese el numero que desea validar como primo: "));
esPrimo(numero)