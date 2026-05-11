def solucion(cad, eli):
    resultado = []
    for char in cad:
        if char not in list(eli):
            resultado.append(char)
    return '.'+".".join(resultado)


eliminar = "aeiouy"
cadena = input().lower()
print(solucion(cadena, eliminar))