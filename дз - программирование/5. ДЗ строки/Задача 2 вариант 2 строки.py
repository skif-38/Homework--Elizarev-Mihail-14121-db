s = input(">> ").strip()
LENGHT = len(s)

prev, cur = "", ""
index = 0
n = 1
while True:
    str_n = str(n)
    cur = prev + str_n
    index += len(str_n)
    if s in cur:
        id = cur.find(s)
        print(index + id - len(cur) + 1)
        break
    prev = cur[-LENGHT:]
    n += 1
