n = int(input())
res = {}
for _ in range(n):
    line = input().strip()
    eng, latin_str = line.split(" - ")
    latins = [l.strip() for l in latin_str.split(',')]
    for l in latins:
        if l not in res:
            res[l] = []
        if eng.strip() not in res[l]:
            res[l].append(eng)
keys = sorted(res.keys())
print(len(res))
for key in keys:
    print(f"{key} - {', '.join(res[key])}")