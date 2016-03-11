def nfruits(fruits, pattern):
    fruits[pattern[0]] -= 1
    if len(pattern) > 1:
        for key in fruits.keys():
            if key != pattern[0]:
                fruits[key] += 1
        nfruits(fruits, pattern[1:])
    return fruits
        
print nfruits( {'A': 1, 'B': 2, 'C': 3} , 'ACB')
