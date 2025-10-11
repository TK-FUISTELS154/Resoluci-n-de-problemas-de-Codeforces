n = int(input())
colores = input()

count = 0
if n == len(colores):
    for i in range(len(colores)-1):
        if colores[i] == colores[i+1]:
            count+=1
    print(count)