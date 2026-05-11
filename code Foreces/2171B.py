def calcular_b(a,n):
    b = []
    for i in range(n-1):
        b.append(a[i+1]-a[i])
    return b

def convertir_a(a):
    return [x if x != -1 else 0 for x in a]

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    print(calcular_b(a,n),abs(sum(calcular_b(a,n))))
    print(convertir_a(a))

