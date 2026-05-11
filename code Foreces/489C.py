def min_max(a, m):
    lista = []
    for i in range(1, m+1):
        if len(str(i)) == int(a):
            lista.append(i)
    return sum(lista)

print(min_max(2, 15))

print(sum(i for i in range(11, 16)))