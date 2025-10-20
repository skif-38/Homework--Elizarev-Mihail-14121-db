
count = int(input("Number from 1 to 64: "))
c = {tuple(map(int, input("Row and column number: ").split())) for _ in range(count)}

count = 0
for r, col in c:
    for row, col1 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if (r + row, col + col1) not in c:
            count += 1

print(count)

