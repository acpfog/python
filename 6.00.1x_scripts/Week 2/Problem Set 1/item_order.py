# Write a function called item_order that takes as input a string named order.
# The string contains only words for the items the customer can order separated by one space.
# The function returns a string that counts the number of each item and consolidates them in
# the following order: salad:[# salad] hamburger:[# hambruger] water:[# water]

def item_order ( order ):

    item1 = "salad"
    item2 = "hamburger"
    item3 = "water"

    word_found = ""
    item1_found = 0
    item2_found = 0
    item3_found = 0

    for i in range ( 0 , len ( order ) + 1 ):
        if i == len ( order) or order[i] == " ":
            if word_found == item1:
                item1_found += 1
            if word_found == item2:
                item2_found += 1
            if word_found == item3:
                item3_found += 1
            word_found = ""
        else:
            word_found += order[i]

    result = "%s:%s %s:%s %s:%s" % ( item1 , item1_found , item2 , item2_found , item3 , item3_found )
    return result

string = "salad water hamburger salad hamburger"
print item_order ( string )
