#Error
t = int(input())
salida = []
for _ in range(t):
    minimos = []
    a, b, n = map(int, input().split())
    for m in range(n,0,-1):
        minimos.append(min(b,(a/m)))
    #print(minimos)    
    salida.append(minimos[-1])

for resultado in salida:
    print(resultado)