#Keep asking the user to input the longest sentence they can without the character “A”.
#Each time a user successfully sets a new longest sentence, print a congratulations message.

max_len = 0
while True:
    sentence = input("Enter the longest sentence without the letter 'a/A': ")
    if 'a' not in sentence.lower() and len(sentence) > max_len:
        max_len = len(sentence)
        print("Congratulations! New longest sentence!")