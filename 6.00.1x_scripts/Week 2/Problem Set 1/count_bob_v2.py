# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2

s = 'azcbobobegghaklopi'
bob = 'bob'
found_bob = 0

for i in range( 0, len( s ) - len ( bob ) + 1 ):
    j = i + len ( bob )
    if bob == s[i:j]:
       found_bob += 1 

print "Number of times bob occurs is: %s" % found_bob
