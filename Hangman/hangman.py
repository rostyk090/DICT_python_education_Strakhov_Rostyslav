import random
print("HANGMAN")
print("The game will be available soon.")
words = ['python', 'javascript', 'php', 'java']
start = 0
english_letters = list("qwertyuiopasdfghjklzxcvbnm")
while (start != 'exit'):
    if start == "play":
        count = 0
        answer_prog = random.choice(words)  # python
        word_list = list(answer_prog)
        letter = ""
        user_word_list_null = "-" * len(answer_prog)
        user_list = list(user_word_list_null)
        user_used = []
        print(user_word_list_null)
        while (count != 8):
            count += 1
            answer_user = str(input('Input a letter:'))
            if answer_user in user_used:
                 print("You have already guessed this letter")
                 count -= 1
                 print(''.join(user_list))
                 continue
            user_used.append(answer_user)
            if answer_user in word_list:
                 if word_list.count(answer_user) >= 2:
                    index = word_list.index(answer_user)
                    user_list[index] = answer_user
                    word_list[index] = '-'
                 index = word_list.index(answer_user)
                 user_list[index] = answer_user
                 count -= 1
            elif answer_user not in english_letters:
                print("Please enter a lowercase English letter")
                continue
            elif len(answer_user) >= 2:
                print("You should input a single letter")
                continue
            elif answer_user not in (user_used and word_list):
                print("That letter does not appear in the word")
            print(''.join(user_list))
            word_list = list(answer_prog)
            if ''.join(user_list) == ''.join(word_list):
                print("You guessed the word!")
                print("You survived!")
                break
        if ''.join(user_list) != ''.join(word_list):
            print("You lost!")
        start = str(input('Type "play" to play the game, "exit" to quit:'))
    elif start == "exit":
        break
    else:
        start = str(input('Type "play" to play the game, "exit" to quit:'))






