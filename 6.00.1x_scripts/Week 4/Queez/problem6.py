
def flatten(aList):
    L = []
    for element in aList:
        if type(element) is not list:
            L.append(element)
        else:
            L += flatten(element)
    return L

print flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
