N = int(input())
x = 0
for i in range(N):
    op = "+" if "+" in (input()) else "-"
    if op == "+":
        x += 1
    else:
        x -= 1
print(x)