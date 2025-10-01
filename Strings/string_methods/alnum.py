#The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.it will returns false even it found the whitespaces in the string

str1 = "WelcomeToTheConsole"
print(str1.isalnum())

str1 = "WelcomeToThe123Console"
print(str1.isalnum())

str1 = "Welcome@ToTheConsole"
print(str1.isalnum())