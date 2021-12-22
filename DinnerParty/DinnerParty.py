import random

print("Enter the number of friends joining (including you):")
count = int(input())
if count <= 0:
    print("No one is joining for the part")
    exit()
print("Enter the name of every friend (including you), each on a new line:")
l_human = {}
for ii in range(count):
    l_human[input()] = 0
print("Enter the total amount:")
general = int(input())
PayOne = round(general / count, 2)
for OneKey in l_human.keys():
    l_human[OneKey] = PayOne
print("""Do you want to use the "Who is lucky?" feature? Write Yes/No:""")
answer = input()

if answer.lower() == "yes":
    lucky = random.choice(list(l_human.keys()))
    print(lucky + " is the lucky one!")
    PayOne_1 = round(general / (count - 1), 2)
    for OneKey in l_human.keys():
        if OneKey == lucky:
            l_human[OneKey] = 0
        else:
            l_human[OneKey] = PayOne_1
    print(l_human)
if answer.lower() == "no":
    print("No one is going to be lucky.")
    print(l_human)

