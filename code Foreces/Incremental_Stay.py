# tiene errores de slaida este codigo 

t = int(input())
salidas_fin = []*t
for _ in range(t):
    n = x if (x := int(input())) > 0 else exit()
    n2 = list(map(int, input().split()))
    if n*2 == len(n2):

        d = [n2[n+i] - n2[i] for i in range(n)]
        d.sort(reverse=True)

        salida = [0]*(n+1)
        for i in range(n):
            salida[i+1] = salida[i] + d[i]

        salidas_fin.append(salida[1:])

for ouput in salidas_fin:

    print(*ouput)
