num=int(input("Enter any a number"))
fact=1
if num<0:
    print("sorry,factorial does not exist for negative numbers")
elif num==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
        print("The factorial of ",num,"is",fact)
