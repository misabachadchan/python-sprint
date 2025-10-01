#witre a program to find out wheter a student is pass or fail if it requires total 40% and atleast 33% in eace subject to pas.Assume 3 subjects and take marks as an input from the user
sub1=int(input("Enter marks 1:"))
sub2=int(input("Enter marks 2:"))
sub3=int(input("Enter marks 3:"))

total_precentage=(sub1+sub2+sub3)/3
print(total_precentage)

if(sub1>=33 and sub2>=33 and sub3>=33 and total_precentage>=40):
    print("pass")
else:
    print("fail")
