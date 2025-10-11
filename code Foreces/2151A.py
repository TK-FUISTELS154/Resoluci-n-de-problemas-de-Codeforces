def count_sublist(n, m, am):
    count = 0
    for i in range(len(am)-m+1):
        sublist = tuple(am[i:i+m])
        if sublist == tuple(sorted(sublist)): # check if sublist is sorted before counting it
            count += 1
    return count

t = int(input())
salida = []
for _ in range(t):
    n, m = map(int, input().split())
    am = input().split()
    am = [int(x) for x in am] # convert string to int
    salida.append(count_sublist(n, m, am))
for sal in salida:
    print(sal)
