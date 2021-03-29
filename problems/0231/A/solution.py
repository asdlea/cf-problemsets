N = int(input())

acum = 0
for _ in range(N):
    x = sum([int(y) for y in input().split(" ")])
    if x>=2:
        acum += 1

print(acum)