N, M = (int(x) for x in input().split())
A = [int(x) for x in input().split()]
t = 0
prev = 1

for i, task in enumerate(A):
    if not task < prev:
        t += task-prev
        prev = task
    else:
        t += N-prev
        t += task
        prev = task
print(t)