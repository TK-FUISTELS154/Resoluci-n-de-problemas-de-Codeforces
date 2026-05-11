t = int(input())
salida = []
for _ in range(t):
    n = int(input())
    s = input()
    ultimo = s[-1]

    ops = 0
    for i in range(n - 1):
        if s[i] != ultimo:
            ops += 1

    salida.append(ops)

for resultado in salida:
    print(resultado)   