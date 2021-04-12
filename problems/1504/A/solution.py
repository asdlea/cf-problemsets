import io
import os
import sys

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

N = int(input())
S = [input().decode().strip() for _ in range(N)]

res = []
for s in S:
    s_len = len(s)
    a = 0
    while a <= s_len + 1:
        # for a in range(s_len+1):
        # s_a = "".join((s[:a], "a", s[a:]))
        s_a = s[:a] + "a" + s[a:]

        if s_a == s_a[::-1]:
            if a == s_len:
                res.append("NO")
                a += 1
                break
            else:
                a += 1
                continue

        res.append("YES")
        res.append(s_a)
        a += 1
        break

sys.stdout.write("\n".join(res))