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
