
n, k =list(map(int,input().split()))
an = list(map(int, input().split()))
count = 0
for num in an:
    if num>=an[k-1] and num > 0 and len(an)==n:
        count+=1
print(count)