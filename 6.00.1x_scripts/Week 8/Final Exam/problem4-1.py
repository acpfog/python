def getSublists ( L , n ):
    r = []
    for i in range ( 0 , len( L ) - n + 1 ):
        t = []
        for j in range ( 0 , n ):
            t.append( L[i+j] )
        r.append( t )
    return r


#L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
#n = 4

L = [1, 1, 1, 1, 4]
n = 2

print getSublists ( L , n )
