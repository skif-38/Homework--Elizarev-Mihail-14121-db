n, m = map(int, input().split())
spisok = []
for _ in range(n):
    row = input().strip()
    spisok.append(tuple(row))
count = 0
for i in range(n):
    for j in range(m):
        if spisok[i][j] == '.':
            valid = True
            if i > 0 and spisok[i-1][j] == '*':
                valid = False
            if i < n-1 and spisok[i+1][j] == '*':
                valid = False
            if j > 0 and spisok[i][j-1] == '*':
                valid = False
            if j < m-1 and spisok[i][j+1] == '*':
                valid = False
            if valid:
                count += 1

print(count)