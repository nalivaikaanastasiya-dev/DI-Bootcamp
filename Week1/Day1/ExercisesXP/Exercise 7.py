#Write code that asks the user for a number and determines whether this number is odd or even.

nuber=int(input('write a number: '))
number=nuber%2
if number==1:
    print('Number is even')
elif number==0:
    print('Number is odd')