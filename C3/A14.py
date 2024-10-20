n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

p = [a[i] + b[j] for i in range(n) for j in range(n)]
q = [c[i] + d[j] for i in range(n) for j in range(n)]

q.sort()

def binary(arr, target, left, right):
    if left >= right:
        return False
    mid = (left + right) // 2
    if arr[mid] == target:
        return True
    if arr[mid] < target:
        return binary(arr, target, mid + 1, right)
    if arr[mid] > target:
        return binary(arr, target, left, mid)

def f():
    for x in p:
        if binary(q, k - x, 0, len(p) - 1):
            return "Yes"
    return "No"

print(f())




#--------------------------
#n, k = map(int, input().split())
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))
#c = list(map(int, input().split()))
#d = list(map(int, input().split()))

#p = [a[i] + b[j] for i in range(n) for j in range(n)]
#q = [c[i] + d[j] for i in range(n) for j in range(n)]

#def f():
#    for i in range(n*n):
#        for j in range(n*n):
#            if k - p[i] == q[j]:
#                return "Yes"
#    return "No"

#print(f())

