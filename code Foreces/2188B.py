#Sin solucionar
# Wrong answer on test 2
def minStudents(s,k):
    matris, student = [], k
    for i in s:
        matris.append(list(map(int, i)))

    if len(matris) > 1:
        for element in matris:
            student += len(element)//3

            if len(element) % 2 != 0 and len(element) >= 5:
                student += 1
        
        if len(matris[0]) == 2 and len(matris[-1]) == 2:
            student += 2

        elif len(matris[0]) == 2 or len(matris[-1]) == 2:
            student += 1

    else:
        if len(matris[0]) >= 3:
            student += len(matris[0])//3
            if len(matris[0]) % 2 != 0 and len(matris[0]) >=5:
                student += 1
        else:
            student += 1
    
    return student
        

t = int(input())
salida = []
comp = True

for _ in range(t):
    n = int(input())
    s = input()
    if n == len(s):
        salida.append(minStudents(s.split('1'), s.count('1')))
    else:
        comp = False
        break

if comp:
    for sal in salida:  
        print(sal)