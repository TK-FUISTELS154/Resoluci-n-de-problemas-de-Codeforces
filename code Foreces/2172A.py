g,c,l = list(map(int, input().split()))
print("check again"if (max(g,c,l) - min(g,c,l))>=10 else f"final {g+c+l-min(g,c,l)-max(g,c,l)}")