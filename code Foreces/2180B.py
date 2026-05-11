t = int(input())

for _ in range(t):
    n = int(input())
    ai = input().split()

    s = ""
    for a in ai:
        if a + s < s + a:
            s = a + s
        else:
            s = s + a

    print(s)
