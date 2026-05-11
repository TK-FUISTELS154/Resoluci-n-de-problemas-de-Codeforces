s = input().strip()
target = "hello"
j = 0

for ch in s:
    # print(f"ch={ch}")
    if j < len(target) and ch == target[j]:
        # print(f"j<len(target) [=] {j} < {len(target)} and ch==target[j][=]{ch}=={target[j]}")
        j += 1

print("YES" if j == len(target)  else "NO")