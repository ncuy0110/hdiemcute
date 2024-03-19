A = []
for i in range(10):
    A.append(int(input()))

for i in range(0, 10, 2):
    A[i], A[i+1] = A[i+1], A[i]

for e in A:
    print(e, end=" ")