def Nhap(m, n):
    P = []
    for i in range(m):
        Q = []
        for j in range(n):
            Q.append(int(input()))
        P.append(Q)
    return P


m = int(input("m="))
n = int(input("n="))

print("A:")
A = Nhap(m, n)

print("B:")
B = Nhap(m, n)

print("C:")
for i in range(m):
    for j in range(n):
        print(A[i][j] + B[i][j], end=" ")
    print()