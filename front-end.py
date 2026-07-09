n = int(input())
a = list(map(int, input().split()))

b = []

for i in range((n+1)//2):
    b.append(a[i])
    if i != n-1-i:
        b.append(a[-(i+1)])

print(*b)
