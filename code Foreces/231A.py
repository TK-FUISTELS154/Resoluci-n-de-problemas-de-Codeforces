def very(lista):
    count=0
    for num in lista:
        if num == 1:
            count += 1

    return count

n = int(input())
salida=0
for _ in range(n):
    if very(map(int, input().split())) >= 2:
        salida += 1
print(salida)
    