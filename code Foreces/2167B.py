t = int(input())
salida = []
for _ in range(t):
    n = int(input())
    a, b = input().split()
    salida.append("YES" if sorted(a) == sorted(b) else "NO")

for resultado in salida:
    print(resultado)