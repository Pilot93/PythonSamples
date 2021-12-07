import sys

j = sys.stdin.readlines()
n = int(j.pop(0))
mem, i, length = 0, 0, 0
while i < n:
    k = int(j.pop(0))
    if k>0:
        if mem < length:
            mem = length
            length = length + 1
    else:
        length = 0 
    i = i + 1
print (mem)
