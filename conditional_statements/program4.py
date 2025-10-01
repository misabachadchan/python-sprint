#Write a program to find whether a given username conatins less than 10 characters or not

#1st method using only characters....

# name=input("Enter username:")

# if(name.isalnum(len(name))<10):
#     print("Less than 10 characters")
# else:
#     print("More than 10 characters")

#2nd method using only alnum characters....

name=input("Enter username:")

if name.isalnum():
    if(len(name)<10):
         print("Less than 10 characters")
    else:
         print("More than 10 characters")

    

