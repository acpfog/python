#
# dict_invert takes in a dictionary with immutable values and returns the inverse of the dictionary.
# The inverse of a dictionary d is another dictionary whose keys are the unique dictionary values in d.
# The value for a key in the inverse dictionary is a sorted list of all keys in d that have the same value in d.
# 
# Here are some examples:
# If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
# If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
# If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}
#
def dict_invert ( d ):
    r = {}
    for key in d.keys():
        if d[key] in r.keys():
            t = r[d[key]]
            t.append( key )
            r[d[key]] = sorted(t)
        else:
            r.update({ d[key] : [ key, ] })
    return r

#d = {1:10, 2:20, 3:30}
#d = {1:10, 2:20, 3:30, 4:30}
d = {4:True, 2:True, 0:True}

print dict_invert ( d )
