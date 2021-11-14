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



