n = int(input())
b = [list(map(int, input().split())) for _ in range(n)]

count = 0

for team in b:
    if sum(team) >= 2:
        count += 1

print(count)
