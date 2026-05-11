def conteo_patas(n):
    if n % 2 == 0:
        return(n // 4) + (((n % 4)//2) if ((n % 4)//2) != 0 else ((n % 4)//2)+1)
    else:
        return 0

salida = []
for _ in range(int(input())):
    salida.append(conteo_patas(int(input())))

for resultado in salida:
    print(resultado)