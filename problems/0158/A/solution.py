def solution(n, k, arr):
    y = arr[k - 1]
    return len([x for x in arr if 0 < x >= y])


n, k = (int(x) for x in input().split())
arr = [int(x) for x in input().split()]

print(solution(n, k, arr))
