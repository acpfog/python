# Write a function nfruits that takes two arguments:
# 
# A non-empty dictionary containing type of fruit and its quantity initially with Python when he leaves home (length < 10)
# A string pattern of the fruits eaten by Python on his journey as observed by Cobra.
# This function should return the maximum quantity out of the different types of fruits that is available with Python when he has reached the campus.
# 
# For example, if the initial quantities are {'A': 1, 'B': 2, 'C': 3} and the string pattern is 'AC' then
# 
# 'A' is consumed, updated values are {'A': 0, 'B': 2, 'C': 3}
# Python buys 'B' and 'C', updated values are {'A': 0, 'B': 3, 'C': 4}
# 'C' is consumed, updated values are {'A': 0, 'B': 3, 'C': 3}
# Now Python has reached the campus. So the function will return 3 that is maximum of the quantities of the three fruits.

def nfruits(fruits, pattern):
    fruits[pattern[0]] -= 1
    if len(pattern) > 1:
        for key in fruits.keys():
            if key != pattern[0]:
                fruits[key] += 1
        nfruits(fruits, pattern[1:])
    return fruits
        
print nfruits( {'A': 1, 'B': 2, 'C': 3} , 'ACB')
