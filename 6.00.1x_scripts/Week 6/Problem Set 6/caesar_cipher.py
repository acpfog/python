# The idea of the Caesar Cipher is to pick an integer and shift every letter of your message by that integer.
# In other words, suppose the shift is k . Then, all instances of the i-th letter of the alphabet that appear in
# the plaintext should become the (i+k)-th letter of the alphabet in the ciphertext. You will need to be careful with
# the case in which i + k > 26 (the length of the alphabet).
# Here is what the whole alphabet looks like shifted three spots to the right:
# 
# Original:  a b c d e f g h i j k l m n o p q r s t u v w x y z
#  3-shift:  d e f g h i j k l m n o p q r s t u v w x y z a b c
# 
# Using the above key, we can quickly translate the message "happy" to "kdssb" (note how the 3-shifted alphabet
# wraps around at the end, so x -> a, y -> b, and z -> c).

import string

shift = 6

cipherDict = {}
alphabet = string.ascii_lowercase
j = shift
l = len(alphabet)
for i in range( l ):
    cipherDict.update({ alphabet[i] : alphabet[j] })
    cipherDict.update({ alphabet[i].upper() : alphabet[j].upper() })
    if j == l - 1:
        j = 0
    else:
        j += 1

for key in sorted(cipherDict):
    print "%s -> %s" % (key, cipherDict[key])

keys = cipherDict.keys()
message_text = "we are taking 6.00.1x"
cipherMessage = ""
for i in range( len(message_text) ):
    if message_text[i] in keys:    
        print cipherDict[message_text[i]]
    else:
        print message_text[i]
#    cipherMessage += cipherDict[ message_text[i] ]
#print cipherMessage
