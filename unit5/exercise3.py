n = int(input("n="))
L = []

for i in range(n):
    L.append(int(input()))

SND = 0
TBC = 0
dem = 0
for e in L:
    # tinh tong so duong
    if e > 0:
        SND += 1
    # tinh tong va dem so luong so chan
    if e % 2 == 0:
        TBC += e
        dem += 1
    
if dem > 0:
    TBC = TBC / dem

print("SND=", SND, sep="")
if TBC == int(TBC):
    print("TBC=", int(TBC), sep="")
else:
    print("TBC=", TBC, sep="")