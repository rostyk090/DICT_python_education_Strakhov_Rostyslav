
class CoffeeMachine:
    def __init__(self, w, m, cb, c, mm):
        self.water = w
        self.milk = m
        self.coffee_beans = cb
        self.cups = c
        self.money = mm

    def remaining(self):
        print('The coffee machine has:')
        print(str(self.water) + ' of water')
        print(str(self.milk) + ' of milk')
        print(str(self.coffee_beans) + ' of coffee beans')
        print(str(self.cups) + ' of disposable cups')
        print(str(self.money) + ' of money')

    def enough(self):
        if self.water < 0:
            return "Sorry, not enough water"
        elif self.milk < 0:
            return "Sorry, not enough milk"
        elif self.coffee_beans < 0:
            return "Sorry, not enough coffee_beans"
        elif self.cups < 0:
            return "Sorry, not enough disposable cups"

    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:')
        answer_user = input()
        if answer_user == str(1):
            self.water -= 250
            self.coffee_beans -= 16
            self.cups -= 1
            self.money += 4
            if CM.enough() is None:
                print('I have enough resources, making you a coffee!')
            else:
                print(CM.enough())
            return 'espresso', self
        elif answer_user == str(2):
            self.water -= 350
            self.milk -= 75
            self.coffee_beans -= 20
            self.cups -= 1
            self.money += 7
            if CM.enough() is None:
                print('I have enough resources, making you a coffee!')
            else:
                print(CM.enough())
            return 'latte', self
        elif answer_user == str(3):
            self.water -= 200
            self.milk -= 100
            self.coffee_beans -= 12
            self.cups -= 1
            self.money += 6
            if CM.enough() is None:
                print('I have enough resources, making you a coffee!')
            else:
                print(CM.enough())
            return 'cappuccino', self
        elif answer_user == 'back':
            return 'back', self

    def fill(self):
        print("Write how many ml of water you want to add:")
        add_water = int(input())
        self.water = self.water + add_water
        print("Write how many ml of milk you want to add:")
        add_milk = int(input())
        self.milk += add_milk
        print("Write how many grams of coffee beans you want to add:")
        add_coffee_beans = int(input())
        self.coffee_beans += add_coffee_beans
        print("Write how many disposable coffee cups you want to add:")
        add_cups = int(input())
        self.cups += add_cups
        return

    def take(self):
        print("I gave you " + str(self.money))
        self.money = 0
        return

    def action(self):
        print('\nWrite action (buy, fill, take, remaining, exit):')
        action_user = str(input())
        if action_user == 'buy':
            CM.buy()
            return 'buy'
        elif action_user == 'fill':
            CM.fill()
            return 'fill'
        elif action_user == 'take':
            CM.take()
            return 'take'
        elif action_user == 'remaining':
            CM.remaining()
            return 'remaining'
        elif action_user == 'exit':
            return 'exit'


while_action = 0
CM = CoffeeMachine(400, 600, 600, 500, 450)
while while_action != 'exit':
    while_action = CM.action()
