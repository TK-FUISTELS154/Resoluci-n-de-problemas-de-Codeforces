t = int(input())
salida = []
for _ in range(t):
    a, b, c, d = map(int, input().split())
    salida.append("YES" if a == b == c == d and (a+b+c+d) > 0 else "NO")

for resultado in salida:
    print(resultado)