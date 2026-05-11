#Logica con mas consumo de recursos, pero mas facil de entender, aunque no es la mejor solucion
# def ordenar(lista):
#     counter = 0
#     ordenado = sorted(lista)
#     while ordenado != lista:
#         pos = 0
#         for num in ordenado:
#             if num !=lista[pos]:
#                 lista.remove(num)
#                 lista.insert(pos,num)
#                 counter += 1
#                 break
#             else:
#                 pos += 1
#     return str(counter)


# t = int(input())
# salida = []
# for _ in range(t):
#     n= int(input())
#     lista = input().split()
#     salida.append(ordenar(lista))

# print("\n".join(salida))



def max_operations(a):
    max_so_far = a[0]
    ops = 0
    for x in a[1:]:
        if x < max_so_far:
            ops += 1
        else:
            max_so_far = x
    return str(ops)

t = int(input())
salida = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    salida.append(max_operations(a))

print("\n".join(salida))