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
