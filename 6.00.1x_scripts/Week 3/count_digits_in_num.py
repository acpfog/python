# Write a function called ndigits, that takes an integer x (either positive or negative) as an argument. This function should return the number of digits in x.

def ndigits ( x ):
    x = abs(x) / 10
    if x > 0:
        return 1 + ndigits ( x )
    else:
        return 1

print ndigits ( -8018975 )
