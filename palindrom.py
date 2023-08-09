Num=int(input('Enter any a numer'))
sum=0
digit=Num
while digit > 0:
    rem=digit%10
    sum=sum*10+rem**3
    digit =digit//10
if (sum==digit):
    print(Num,'Is a palindrom number ')
else:
    print(Num,'is not a palindrom number ')
