paises = input("Ingrese la lista de paises separados por coma")
paises = list(set(paises.split(',')))
paises.sort()
print(paises)