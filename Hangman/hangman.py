import random
print('HANGMAN')
print('The game will be available soon')
print("Guess the word:")
answer = input()
if answer == "python":
    print("You survived!")
else:
    print("You lost!")
import random
print("HANGMAN")
print("The game will be available soon.")
list_words = ['python', 'javascript', 'php', 'java']
answer_prog = random.choice(list_words)
print("Guess the word:")
answer == input()
if answer == answer_prog:
    print("You survived!")
else:
    print("You lost!")
import random
print("HANGMAN")
print("The game will be available soon.")
list_words = ['python', 'javascript', 'php', 'java']
answer_prog = random.choice(list_words)
help_prog = answer_prog[0] + answer_prog[1] + answer_prog[2] + '-' * (len(answer_prog) -3)
print("Guess the word " + help_prog + ":")
answer = input()
if answer == answer_prog:
    print("You survived!")
else:
    print("You lost!")
import random
print("HANGMAN")
print("The game will be available soon.")
words = ['python', 'javascript', 'php', 'java']
answer_prog = random.choice(words)  # python
word_list = list(answer_prog)
user_word_list_null = "-" * len(answer_prog)
user_list = list(user_word_list_null)
print(user_word_list_null)
count = 0
while count != 8:
    count += 1
    answer_user = str(input('Input a letter:'))
    if answer_user in word_list:
        if word_list.count(answer_user) >= 2:
            index = word_list.index(answer_user)
            user_list[index] = answer_user
            word_list[index] = '-'
        index = word_list.index(answer_user)
        user_list[index] = answer_user
    else:
        print("That letter does not appear in the word")
    print(''.join(user_list))
print("Thanks for playing!")
print("We will see how well you di in the text stage")


