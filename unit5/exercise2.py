def Input():
    L = []
    n = int(input("n="))
    for i in range(n):
        L.append(int(input()))

    return L

def Search(L):
    if len(L) == 0:
        return None, None
    mx, mi = L[0], L[0]
    for e in L:
        # neu phan tu e lon hon max -> max = e
        if e > mx:
            mx = e
        # neu phan tu e nho hon min -> min = e
        if e < mi:
            mi = e
    return mx, mi

def Output(max, min):
    print(max, min)

L = Input()
max, min = Search(L)
Output(max, min)