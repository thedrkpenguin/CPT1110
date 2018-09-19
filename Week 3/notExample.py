number = int(input("Enter a number: "))
text = str(input("Enter a string of text: "))
text1 = str(input("Enter another string of text: "))

#if not (number > 5 and text == "Paul"): 
#    print("True")
#else:
#    print("False")

if not ((number > 5 or text == "Paul") and text1 == "Bob"): 
    print("True")
else:
    print("False")


#if not number < 5:  # if number >= 5
#    print("TRUE")
#else:
#    print("FALSE")
