n = int(input())
num = n
salida = 0
for i in range(5,0,-1):
    salida+=num//i
    num=num%i
print(salida)
