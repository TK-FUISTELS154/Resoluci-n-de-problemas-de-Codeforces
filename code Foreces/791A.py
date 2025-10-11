a, b = list(map(int,input().split()))
if a<=b:
    ciclo = 0
    while True:
        if a>b:
            print(ciclo)
            break
        else:
            ciclo+=1
            a*=3
            b*=2
