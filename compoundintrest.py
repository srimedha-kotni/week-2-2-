p=float(input("enter principle amount:"))
r=float(input("enter rate of intrest:"))
t=int(input("enter time period:"))
a=p*(1+(r/100))**t
ci=a-p
print("compound intrest is: ",ci)
