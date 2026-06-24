n = int(input())
# Read the list correctly as flat integers
a = list(map(int, input().split()))

# Sort the list in ascending order
a.sort()

# Print the list elements separated by a space
print(*a)
