n = int(input("n="))
A = []
for i in range(n):
    A.append(int(input()))

Tong = 0
for i in range(1, n, 2):
    Tong += A[i]

print("Tong=", Tong, sep="")