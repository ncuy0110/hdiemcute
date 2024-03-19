n = int(input("n="))
m = int(input("m="))

print("L1:")
L1 = []
for i in range(n):
    L1.append(int(input()))

print("L2:")
L2 = []
for i in range(m):
    L2.append(int(input()))

L3 = []
for e in L1:
    if e in L2 and e not in L3:
        L3.append(e)

print("L3: ", end="")
for e in L3:
    print(e, end=" ")