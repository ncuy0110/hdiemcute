def Input():
    L = []
    n = int(input("n="))
    for i in range(n):
        L.append(int(input()))

    return L

def FirstAndLast(L):
    return [L[0], L[-1]]

def Search(L, x):
    return x in L

L = Input()
x = int(input("x="))
print(FirstAndLast(L))
print(Search(L, x))