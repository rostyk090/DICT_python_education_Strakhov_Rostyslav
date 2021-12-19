from random import choice
count = int(input('Enter the number of friends joining (including you):\n'))
n = {}
l = []
if count >= 0:
    for i in range(count):
        print('Enter the name of every friend (including you), each on a new line:')
        name = input()
        n[name] = 0
        l.append(name)
else:
    print('No one is joining for the party')
print(n)
print('Enter the total amount:')
general = int(input())
for name in n:
    n[name] = round(general / count, 2)
lucky = choice(l)
answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
if answer == 'Yes' or 'yes':
    print(lucky + ' is the lucky one!')
else:
    print("No one is going to be lucky")
