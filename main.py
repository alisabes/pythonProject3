a = input()
m = a.split()

for i in m:
    d = len(i)
    if d % 2 == 1:
        left = i[:d // 2]
        right = i[d // 2 + 1:]
        right = right[::-1]
    else:
        left = i[:d // 2]
        right = i[d // 2:]
        right = right[::-1]
    if left == right:
        print(i)


