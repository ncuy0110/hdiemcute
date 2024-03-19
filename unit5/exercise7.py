n = int(input("n="))

L = []
for i in range(n):
    L.append(int(input()))

M = []
for e in L:
    if e not in M:
        M.append(e)

for e in M:
    print(e, end=" ")