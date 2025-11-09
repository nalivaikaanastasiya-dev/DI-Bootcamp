while True:
    str_inp=input('Please enter a string of exactly 10 characters: ')
    if len(str_inp)<10:
        print('String not long enough.')
    elif len(str_inp)>10:
        print('String too long.')
    elif len(str_inp)==10:
        print('Perfect string.')
        print("First character:", str_inp[0])
        print("Last character:", str_inp[-1])
        if len(str_inp) == 10:
            new_str = ''
            for char in str_inp:
                new_str +=char
                print(new_str1)
            break
    else:
        print("String is not 10 characters long. Try again.")
