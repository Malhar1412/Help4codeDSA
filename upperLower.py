char=str(input("Enter a character to check the upper or lower case or any special character "))
if char==char.upper():
    print("the character is in upper case")
elif char==char.lower():
    print("the character is in lower case")
else:
    print("the character is a special character")