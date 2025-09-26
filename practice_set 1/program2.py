# Write a program to fill in a letter template given below with name and date
# letter='''Dear <|Name|>,You are selected! <|date|>'''

import datetime
name=input("Enter your name:")
d=datetime.date(2025,9,26)
print("Dear",name,"\nYou are selected!\n",d)
