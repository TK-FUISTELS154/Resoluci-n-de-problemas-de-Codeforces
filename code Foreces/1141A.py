def solucion(ini, fin):
    if fin % ini != 0:
        return -1
    
    x = fin // ini
    count = 0
    
    while x % 2 == 0:
        x //= 2
        count += 1
        
    while x % 3 == 0:
        x //= 3
        count += 1
    
    if x == 1:
        return count
    else:
        return -1


ini, fin = map(int, input().split())
print(solucion(ini, fin))
