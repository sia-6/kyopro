n = int(input())
a = list(map(int, input().split()))

l = [a[0]] * n
r = [a[n - 1]] * n
for i in range(1, n):
    l[i] = max(l[i - 1], a[i])
    r[n - i - 1] = max(a[n - i - 1], r[n - i])

d = int(input())
for _ in range(d):
    x, y = map(int, input().split())
    print(max(l[x - 2], r[y]))