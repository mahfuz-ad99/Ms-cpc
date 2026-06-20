a = input()

distinct = []

for ch in a:
    if ch not in distinct:
        distinct.append(ch)

if len(distinct) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
