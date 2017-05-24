
def genPrimes():
    x = 2
    plist = [x,]
    while True:
        for i in range(len(plist)):
            if x % plist[i] == 0:
                break
        if i >= len(plist)-1:
            plist.append(x)
            yield x
        x += 1

for n in genPrimes():
    print n
