#Write code that asks the user for their name and determines whether or not you have the same name. Print out a funny message based on the outcome.

my_name='Anastasiya'
your_name = str(input('Write your name: '))
if my_name==your_name:
    print('Wow! We are name twins!')
elif my_name!=your_name:
    print('My name wins!')