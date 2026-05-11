# error en prueba 10
# def can_kill(h, ai):
#     k = [h]
#     for i in range(len(ai)-1):
#         k.append(ai[i+1] - ai[i])
#     k.sort()
#     return resultado(k,h)

# def resultado(k,h):
#     daño = 0
#     for i in range(len(k)):
#         prom = redondear((h-daño)/len(k[i:]))
#         if prom <=k[i]:
#             return prom
#         else:
#             daño += k[i]

# def redondear(num):
#     if (num-int(num)) == 0:
#         return int(num)
#     else:
#         return int(num) + 1

# t = int(input())
# salida = []
# for _ in range(t):
#     n , h = map(int, input().split())
#     ai = list(map(int, input().split()))
#     salida.append(str(can_kill(h, ai)))

# print("\n".join(salida))

def can_kill(k, h, ai):
    total = 0
    for i in range(len(ai) - 1):
        total += min(k, ai[i+1] - ai[i])
    total += k
    return total >= h


t = int(input())
salida = []
for _ in range(t):
    n, h = map(int, input().split())
    ai = list(map(int, input().split()))
    
    left, right = 1, h
    ans = h
    
    while left <= right:
        mid = (left + right) // 2
        if can_kill(mid, h, ai):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    
    salida.append(str(ans))

print("\n".join(salida))