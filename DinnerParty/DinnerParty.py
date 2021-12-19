print('Enter the number of friends joining (including you):')
count = int(input())
n = {}
if count >= 0:
    for i in range(count):
        print('Enter the name of every friend (including you), each on a new line:')
        name = input()
        n[name] = 0
else:
    print('No one is joining for the party')
print(n)
print('Enter the total amount:')
general = int(input())
sum_one = round(general / count, 2)
for name in n:
    n[name] = sum_one
