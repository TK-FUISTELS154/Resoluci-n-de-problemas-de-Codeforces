def lozas(n, m, a):
    loza = 0
    if n%a == 0:
        loza = n//a
    else:
        loza = n//a + 1
    if m%a == 0:
        loza *= m//a
    else:
        loza *= m//a + 1
    return str(loza)


n, m, a = list(map(int, input().split()))
print(lozas(n, m, a))

