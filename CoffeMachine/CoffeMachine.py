print("""Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!""")
coffee_water = 200
coffee_milk = 50
coffee_beans = 15
count_cups = int(input("\nWrite how many cups of coffee you will need:"))
water = count_cups * coffee_water
milk = count_cups * coffee_milk
beans = count_cups * coffee_beans
print('For ' + str(count_cups) + ' cups of coffee you will need:')
print(str(water) + ' ml of water')
print(str(milk) + ' ml of milk')
print(str(beans) + ' g of coffee beans')
print("Write how many ml of water the coffee machine has:")
water = int(input())
print("Write how many ml of milk the coffee machine has:")
milk = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
beans = int(input())
print("Write how many cups of coffee you will need:")
cups = int(input())
p_water = water // coffee_water
p_milk = milk // coffee_milk
p_beans = beans // coffee_beans
number = min([p_water, p_milk, p_beans])
if number == cups:
    print("Yes, I can make that amount of coffee")
elif number > cups:
    print("Yes, I can make that amount of coffee (and even " + str(number - cups) + " more than that)")
else:
    print("No, I can make only " + str(number) + " cups of coffee")
water = 400
milk = 540
coffee_beans = 120
cups = 9
money = 550
def remaining():
    print('The coffee machine has:')
    print(str(water) + ' of water')
    print(str(milk) + ' of milk')
    print(str(coffee_beans) + ' of coffee beans')
    print(str(cups) + ' of disposable cups')
    print(str(money) + ' of money' )
def enough():
    global water
    global milk
    global coffee_beans
    global money
    if water < 0:
        return "Sorry, not enough water"
    elif milk < 0:
        return "Sorry, not enough milk"
    elif coffee_beans < 0:
        return "Sorry, not enough coffee_beans"
    elif cups < 0:
        return "Sorry, not enough disposable cups"
def buy():
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:')
    global water
    global milk
    global coffee_beans
    global money
    global cups
    answer_user = input()
    if answer_user == str(1):
        water -= 250
        coffee_beans -= 16
        cups -= 1
        money += 4
        if enough() == None:
            print('I have enough resources, making you a coffee!')
        else:
            print(enough())
        return 'espresso'
    elif answer_user == str(2):
        water -= 350
        milk -= 75
        coffee_beans -= 20
        cups -= 1
        money += 7
        if enough() == None:
            print('I have enough resources, making you a coffee!')
        else:
            print(enough())
        return 'latte'
    elif answer_user == str(3):
        water -= 200
        milk -= 100
        coffee_beans -= 12
        cups -= 1
        money += 6
        if enough() == None:
            print('I have enough resources, making you a coffee!')
        else:
            print(enough())
        return 'cappuccino'
    elif answer_user == 'back':
        return 'back'
def fill():
    global water
    global milk
    global coffee_beans
    global money
    global cups
    print("Write how many ml of water you want to add:")
    add_water = int(input())
    water += add_water
    print("Write how many ml of milk you want to add:")
    add_milk = int(input())
    milk += add_milk
    print("Write how many grams of coffee beans you want to add:")
    add_coffee_beans = int(input())
    coffee_beans += add_coffee_beans
    print("Write how many disposable coffee cups you want to add:")
    add_cups = int(input())
    cups += add_cups
def take():
    global money
    print("I gave you " + str(money))
    money = 0
def action():
    print('\nWrite action (buy, fill, take, remsining, exit):')
    action_user =str(input())
    if action_user == 'buy':
        buy()
        return 'buy'
    elif action_user == 'fill':
        fill()
        return 'fill'
    elif action_user == 'take':
        take()
        return 'take'
    elif action_user == 'remaining':
        print('')
        remaining()
        return 'remaining'
    elif action_user == 'exit':
        return 'exit'
while_action = 0
while while_action != 'exit':
    while_action = action()