#Write code that will ask the user for their height in centimeters.
#If they are over 145 cm, print a message that states they are tall enough to ride.
#If they are not tall enough, print a message that says they need to grow some more to ride.

hight=float(input('What is your height in centimeters? '))
if hight>= 145:
    print('You are tall enough to ride!')
elif hight <145:
    print('Sorry, you are not tall enought!')