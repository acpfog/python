#
# isPalindrome() returns True if aString is a palindrome (reads the same forwards or reversed) and False otherwise.
# Do not use Python's built-in reverse function or aString[::-1] to reverse strings.
#

def isPalindrome(aString):
    aString = aString.lower()
    aString = aString.replace(" ", "")
    aString = aString.replace(".", "")
    aString = aString.replace(",", "")
    aString = aString.replace(":", "")
    aString = aString.replace("!", "")
    aString = aString.replace("?", "")
    if len(aString) > 1: 
        if aString[0] == aString[-1]:
            return isPalindrome(aString[1:-1])
        else:
            return False
    else:
        return True
