n = int(input("n="))
A = []
for i in range(n):
    A.append(int(input()))

B = []
for i in range(n-1, -1, -1):
    B.append(A[i])

for e in B:
    print(e, end=" ")
print()

# sap xep noi bot(Bubble sort)
for i in range(0, n - 1):
    for j in range(i+1, n):
        if B[i] > B[j]:
            B[i], B[j] = B[j], B[i]
            
for e in B:
    print(e, end=" ")