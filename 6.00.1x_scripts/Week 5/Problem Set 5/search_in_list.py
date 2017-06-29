# 
# search() is a version of linear search that used the fact that a set of elements is sorted in increasing order
# newsearch() is an alternative version of search()
#

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False

print "1"
print search([], 5)
print newsearch([], 5)

print "2"
print search([1,2,3,4,5], 1)
print newsearch([1,2,3,4,5], 1)

print "3"
print search([1,2,3,4,5], 3)
print newsearch([1,2,3,4,5], 3)

print "4"
print search([1,2,3,4,5], 5)
print newsearch([1,2,3,4,5], 5)

print "5"
print search([1,2,3,4,5], 0)
print newsearch([1,2,3,4,5], 0)

print "6"
print search([1,2,3,4,5], 6)
print newsearch([1,2,3,4,5], 6)

print "7"
print search([1,2,3,4,5,6], 1)
print newsearch([1,2,3,4,5,6], 1)

print "8"
print search([1,2,3,4,5,6], 3)
print newsearch([1,2,3,4,5,6], 3)

print "9"
print search([1,2,3,4,5,6], 4)
print newsearch([1,2,3,4,5,6], 4)

print "10"
print search([1,2,3,4,5,6], 6)
print newsearch([1,2,3,4,5,6], 6)

print "11"
print search([1,2,3,4,5,6], 0)
print newsearch([1,2,3,4,5,6], 0)

print "12"
print search([1,2,3,4,5,6], 7)
print newsearch([1,2,3,4,5,6], 7)
