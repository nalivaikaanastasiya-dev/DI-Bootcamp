#Ask the user to input a month (1 to 12).
#Display the season of the month received :
#Spring runs from March (3) to May (5)
#Summer runs from June (6) to August (8)
#Autumn runs from September (9) to November (11)
#Winter runs from December (12) to February (2)

number=int(input('Write a month number (from 1 to 12): '))
spring=[3, 4, 5]
summer=[6, 7, 8]
autumn=[9, 10, 11]
winter=[12, 1, 2]
if number in spring:
    print('it is Spring')
elif number in summer:
    print('it is Summer')
elif number in autumn:
    print('it is autumn')
elif number in winter:
    print('it is winter')