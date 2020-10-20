from collections import deque
d = deque()
for _ in range(int(input())):
    var1, *var2 = input().split()
    getattr(d, var1)(*var2) # this what I got lost on. getattr() method
[print(x, end=' ') for x in d] 
