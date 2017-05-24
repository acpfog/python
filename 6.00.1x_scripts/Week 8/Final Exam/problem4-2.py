def getSublists(L, n):
    r = []
    for i in range(0, len( L ) - n + 1):
        t = []
        for j in range(0, n):
            t.append( L[i+j] )
        r.append( t )
    return r

def longestRun(L):
    for i in range(1, len(L)+1):
        for a in getSublists(L, i):
            if a == sorted(a):
                x = len(a)
    return x

#L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
#L = [0]
L = [7, 4, 1, -7, -11]
print longestRun(L)
