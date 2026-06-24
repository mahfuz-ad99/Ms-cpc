a = int(input())
x = 0

for _ in range(a):
    operation = input()
    # Check the specific line for the character '+'
    if "+" in operation:
        x += 1
    else:
        x -= 1

print(x)
