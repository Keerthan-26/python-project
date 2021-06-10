import random
response=(input("Think one number in mind then enter ok\n"))
number=random.randint(0,100)
while response!='ok':
    exit
response=(input("Double the number and enter ok\n"))
x=number*2
while response!='ok':
  exit
response=(input("Add 10 to the result then enter ok\n"))
while response!="ok":
  exit
x+=10
response=(input("divide with 2 the result which you obtained then enter ok\n"))

while response!="ok":
  exit
x=x//2
response=(input("subtract number first you thought from the result then enter ok\n"))
while response!="ok":
  exit
x=x-number
print('The result is',x)
