ch = ord(input("Enter any single chr:"))
if ch>=65 and ch <=90:
 print("upper case")
elif ch>=97 and ch<=122:
 print("lower case")
elif ch>=48 and ch<=57:
 print("Digit")
else:
 print("special character")