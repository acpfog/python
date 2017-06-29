#
# dotProduct() returns the sum of the pairwise products of listA and listB.
# You should assume that listA and listB have the same length and are two lists of integer numbers.
# For example, if listA = [1, 2, 3] and listB = [4, 5, 6], the dot product is 1*4 + 2*5 + 3*6, meaning your function should return: 32
#

def dotProduct(listA, listB):
    result = 0
    for i in range(len(listA)):
        result += listA[i] * listB[i]
    return result

print dotProduct([1, 2, 3], [4, 5, 6])

