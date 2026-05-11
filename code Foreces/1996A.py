def conteo_patas(n):
    return(n // 4)+((n % 4)//2)

salida = []
for _ in range(int(input())):
    salida.append(conteo_patas(int(input())))

for resultado in salida:
    print(resultado)