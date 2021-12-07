import sys
n = int(sys.stdin.readline())
j, i = 0, 0
min = -pow(2,32)
ans = []
while i < n:
    j = int(sys.stdin.readline())
    if j > min:
        ans.append(j)
        min = j
    i = i + 1
print (ans)
