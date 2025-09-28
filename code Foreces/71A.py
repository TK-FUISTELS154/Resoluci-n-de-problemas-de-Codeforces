n = int(input())
palabras=[]
for _ in range(n):
    palabras.append(list(input()))
for palabra in palabras:
    if len(palabra)<=10:
        salida=""
        for letra in palabra:
            salida += letra
        print(salida)
    else:
        print(f"{palabra[0]}{(len(palabra)-2)}{palabra[len(palabra)-1]}")
