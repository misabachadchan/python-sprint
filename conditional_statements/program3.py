#write a program to calculate the grade of a student from his marks from the following scheme 
# 90-100=Excellent 
# 80-90=A
# 70-80=B
# 60-70=C 
# 50-60=D 
# <50=F

marks=int(input("Enter the marks:"))

if(marks>=90 and marks<=100):
    print("Excellent......")
elif(marks>=80 and marks<=90):
    print("A Grade")
elif(marks>=70 and marks<=80):
    print("B Grade") 
elif(marks>=60 and marks<=70):
    print("C Grade")
elif(marks>=50 and marks<=60):
    print("D Grade")
else:
    print("Fail.......!!!!")