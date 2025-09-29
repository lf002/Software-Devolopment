customer = input("Welcome, what is your name? ")

# Step 2 
starting_balance = 5000.25

# Step 3
print("Welcome,", customer)
print("Your starting balance is: $" + str(starting_balance))

# Step 4 
pay_check = float(input("How much of your paycheck would you like to deposit? "))
print("You chose to deposit a total of $", pay_check)

# Step 5 
expenditure_item = input("What did you buy with your money? ")

# Step 6 
expense_amount = float(input("How much was this item? "))

# Step 7 
def checking_balance(customer_name, balance, deposits, expense_item, expense_amount):
    new_balance = balance + deposits - expense_amount
    print("Hello,", customer_name)
    print("Your deposit: $", deposits)
    print("You spent $", expense_amount, "on", expense_item)
    print("Your new balance is: $", new_balance)
    return new_balance

# Step 8
checking_balance(customer, starting_balance, pay_check, expenditure_item, expense_amount)