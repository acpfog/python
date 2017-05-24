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
