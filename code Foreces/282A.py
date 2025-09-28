n = int(input())
salida = 0
for _ in range(n):
    x = input()
    if x.count("+")==2 and x.count("X") == 1:
        salida +=1
    elif x.count("-")==2 and x.count("X") == 1:
        salida -=1
print(salida)