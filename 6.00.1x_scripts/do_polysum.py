# Regular Polygons: polysum
# A regular polygon has 'n' number of sides. Each side has length 's'.
# * The area of regular polygon is: (0.25*n*s^2)/tan(pi/n)
# * The perimeter of a polygon is: length of the boundary of the polygon
# Write a function called 'polysum' that takes 2 arguments, 'n' and 's'.
# This function should sum the area and square of the perimeter of the regular polygon.
# The function returns the sum, rounded to 4 decimal places.

import math

def polysum( n, s ):
    area = ( 0.25 * n * s ** 2 ) / math.tan ( math.pi / n )
    perimeter = n * s
    result = area + perimeter ** 2
    result = round( result, 4 )
    return result

print("A regular polygon has 'n' number of sides. Each side has length 's'.")
sides = int(raw_input("Enter number of sides: "))
length = float(raw_input("Enter length of a side: "))
if ( sides < 3 ):
    print ("A regular polygon cannot have less than 3 sides")
else:
    sides = float(sides)
    print "The result is %s" % polysum ( sides , length )
