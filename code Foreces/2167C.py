salida = []
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    has_even = any(x % 2 == 0 for x in a)
    has_odd = any(x % 2 == 1 for x in a)

    if has_even and has_odd:
        salida.append(sorted(a))
    else:
        salida.append(a)
        
for resultado in salida:
    print(*resultado)