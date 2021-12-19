print("""Loan principal: 1000
Month 1: repaid 250
Month 2: repaid 250
Month 3: repaid 500
The loan has been repaid!""")
import math
print('Enter the loan principal:')
lp = int(input())
print("""What do you want to calculate?
type "m" – for number of monthly payments
type "p" – for the monthly payment:""")
choice = input()
if choice == 'm':
    print('Enter the monthly payment:')
    mp = int(input())
    print('It will take ' + str(math.ceil(lp / mp)) + ' months to repay the loan')
else:
    print('Enter the number of months:')
    nm = int(input())
    pm = math.ceil(lp / nm)
    LastPay = lp - (nm - 1) * pm
    if LastPay == pm:
        print('Your monthly payment = ' + str(pm))
    else:
        print('Your monthly payment = ' + str(pm) + ' and the last payment = ' + str(LastPay))