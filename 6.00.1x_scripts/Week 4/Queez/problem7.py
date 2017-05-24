
def dict_interdiff(d1, d2):
    r1 = {}
    r2 = {}
    for key in d1.keys() + d2.keys():
        if key in d1.keys() and key in d2.keys():
            r1[key] = f(d1[key], d2[key])
        elif key in d1.keys():
            r2[key] = d1[key]
        elif key in d2.keys():
            r2[key] = d2[key]
    return ( r1 , r2 )

#def f(a, b):
#    return a + b

def f(a, b):
    return a > b

#d1 = {1:30, 2:20, 3:30, 5:80}
#d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
print dict_interdiff(d1, d2)
