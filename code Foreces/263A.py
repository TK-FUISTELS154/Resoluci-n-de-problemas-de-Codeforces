matris = []
for _ in range(5):
    matris += list(map(int, input().split()))

x = (matris.index(1)%5)+1
y = (matris.index(1)//5)+1

print(abs(x-3)+abs(y-3))

