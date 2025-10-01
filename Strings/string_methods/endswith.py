#The endswith() method checks if the string ends with a given value. If yes, then return True, else return False.

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))


str1 = "Welcome to the Console !!!"
print(str1.endswith("Console"))


#We can even also check for a value in-between the string by providing start and end index positions.

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))