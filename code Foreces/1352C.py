def num(n,k):
    rev = 0
    ultimo = k
    while ((ultimo//n)-rev) >= 1:
        num = rev
        rev = ultimo//n
        ultimo += (ultimo//n)-num
    else:
        return str(ultimo)
    
# genera la lista excluyendo los multiplos de n y muestra el numero de la posicion k
def generate(n, k, extra):
    lista = [i for i in range(1,k+extra) if i % n != 0]
    return lista, len(lista) - extra, str(lista[k+1]) if k+1 < len(lista) else "El la posicion k no existe en el rango"


t = int(input())
salida = []
for _ in range(t):
    n, k = map(int, input().split())
    salida.append(num(n, k))

print("\n".join(salida))