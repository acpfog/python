#
# A generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...
#

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
