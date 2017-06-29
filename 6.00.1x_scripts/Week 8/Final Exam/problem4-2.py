#
# longestRun, which takes as a parameter a list of integers named L (assume L is not empty).
# This function returns the length of the longest run of monotonically increasing numbers occurring in L.
# A run of monotonically increasing numbers means that a number at position k+1 in the sequence is
# either greater than or equal to the number at position k in the sequence.
#
# For example, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] then your function should return the value 5
# because the longest run of monotonically increasing integers in L is [3, 4, 5, 7, 7].
#

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
