#Compound interest
p=int(input("Enter the principle:"))
t=int(input("Enter the time:"))
r=float(input("Enter the rate of intereset:"))

amount=p*((1+r/100)**t)
compound_interest=amount-p


print("Amount is ",amount)
print("Compound interest is ",compound_interest)