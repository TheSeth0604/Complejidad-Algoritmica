def divideyVenceras_Mayor(arreglo, ini, fin):
    mayor = 1

    if (ini >= fin - 2):
        
        if (arreglo[ini] > arreglo[ini-1]):
            return arreglo[ini];
    
    else:
        return arreglo[ini - 1]

    mayor = divideyVenceras_Mayor(arreglo, ini - 1, fin)

    if (arreglo[ini] > mayor):
        return arreglo[ini]
    
    else:
        return mayor

    
arreglo = [6, 4, 8, 90, 12, 56, 7, 1, 63]
mayor = divideyVenceras_Mayor(arreglo, 0, 9)
print("El maximo numero en el arreglo es: ", mayor)
