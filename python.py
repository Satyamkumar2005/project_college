# it is use for comment:
print(2+3)
print(2+3-2*5/2//5%1)
print(2**2)
text=30
print(text+2)
print(round(1.76,1))
word='python'
print(word[0])
print(len(word))
square=[3,6,9,0,1]
print(square[3])
square.append(10)
print(square)
cube=[2,12,21,33]
new=[square,cube]
print(new[1][2])
a,b=0,1
while a<10:
    print(a,end=',')
    a,b=b,a+b
x=int(input("Please enter number"))
if x<10:
    print("Satyam")
elif x==12:
    print("Maneesh")
else:
    print("Aalok")
for i in square:
    print(i)
users={'hans': 'active','Satyam':'inactive'}
for user, sc in users.copy().items():
    if sc=='inactive':
        del users[user]
print(users)