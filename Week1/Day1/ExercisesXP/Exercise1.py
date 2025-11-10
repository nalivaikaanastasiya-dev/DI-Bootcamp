#Print the following output using one line of code:

#Hello world
#Hello world
#Hello world
#Hello world

print(("Hello world\n") * 4)

#Write code that calculates the result of:

#(99^3)*8 (meaning 99 to the power of 3, times 8).

print((99**3)*8)

#Predict the output of the following code snippets:
#Coment what is your guess, then run the code and compare

#Example:

# 15 < 8 #False
# 5 < 3
# 3 == 3
# 3 == "3"
# "3" > 3
# "Hello" == "hello"

5 < 3 #False
3 == 3 #True
3 == "3" #False
"3" > 3 #TypeError
"Hello" == "hello" #False

#Create a variable called computer_brand which value is the brand name of your computer.
#Using the computer_brand variable, print a sentence that states the following:
#"I have a <computer_brand> computer."

computer_brand='ASUS'
print(f'I have {computer_brand} computer')

#Create a variable called name, and set it’s value to your name.
#Create a variable called age, and set it’s value to your age.
#Create a variable called shoe_size, and set it’s value to your shoe size.
#Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2, and 3.
#Have your code print the info message.
#Run your code.

name='Anastasiya'
age=30
shoe_size=38
info=f'My name is {name}, I am {age} years old, my shoe size is {shoe_size} and I have 2 rats.'
print(info)

#Create two variables, a and b.
#Each variable’s value should be a number.
#If a is bigger than b, have your code print "Hello World".

a=89
b=73
if a>b:
    print('Hello world')

#Write code that asks the user for a number and determines whether this number is odd or even.

nuber=int(input('write a number: '))
number=nuber%2
if number==1:
    print('Number is even')
elif number==0:
    print('Number is odd')

#Write code that asks the user for their name and determines whether or not you have the same name. Print out a funny message based on the outcome.

my_name='Anastasiya'
your_name = str(input('Write your name: '))
if my_name==your_name:
    print('Wow! We are name twins!')
elif my_name!=your_name:
    print('My name wins!')

#Write code that will ask the user for their height in centimeters.
#If they are over 145 cm, print a message that states they are tall enough to ride.
#If they are not tall enough, print a message that says they need to grow some more to ride.

hight=float(input('What is your height in centimeters? '))
if hight>= 145:
    print('You are tall enough to ride!')
elif hight <145:
    print('Sorry, you are not tall enought!')
