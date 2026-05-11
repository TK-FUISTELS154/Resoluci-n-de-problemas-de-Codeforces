t = int(input())
salida = []
for _ in range(t):
    n = int(input())
    ai = list(map(int, input().split()))
    salida.append(max(ai))

for res in salida:
    print(res)