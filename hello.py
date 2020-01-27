#This is a python comment in my first python app.
#This variable contains an integer.
quantity = 12
#This variable contains a float.
unit_price = 26.99
#This vrbl contains the result of multipying quantitiy times unit price.
extended_price = quantity * unit_price
#show the results 
print()
print()
print(extended_price)
print()
print("test\nbob\nknob\nand chill\n")
first_name = "Andrew"
last_name = "Cousins"
print(first_name, last_name)
first_name="Andrew" ; last_name="Cousins"
print(first_name, last_name)
first_name = "Andrew" ; last_name = "Cousins" ; print(first_name, last_name)
firstname = "Andrew"
print(firstname)
print()
blurb = "Disapointment is a function of expectation"
print(blurb)
print()
boobear = "Kieran is the greatest music producer, and the greatest musician\nin the family"
print(boobear)
print()
print("The below false statement is not to be confused with the statement about kieran\nabove. That was merely an outcome of a math function.")
print()
x = 10
if x == 0:
    print("x is zero)")
else:
        print(x is ",x")
        print("All done")
print()
print(firstname)
print()
print()
#second math function but same function
quantity = 44
unit_price = 10000
extended_price = quantity * unit_price 
print(extended_price)
print()
print()
#Formating with f strings.
dogs_name = "Seamas"
print(f"hello {dogs_name}")
print()
print(f"The best dog ever was {dogs_name}, and {firstname} was his master, and his last name is {last_name}.")
print()
print(f"Subtotal: ${quantity * unit_price:,.2f}")
bottles = 24
botprice = 2
print(f"total: ${bottles * botprice:,.2f}")
print()
sales_tax_rate = .1300
print(f"Sales tax Rate {sales_tax_rate}")
print()
print(f"Sales tax Rate {sales_tax_rate:.2%}")
print()
# Mulitiline format Strings
user1 = "Alberto"
user2 = "Babs"
user3 = "Carlos"
output=f"{user1} \n{user2} \n{user3}"
print(output)
print()
print()
#The folowing is an extended example of multiline format strings \nto demonstrate more possibilities in python strings.")
print()
user1 = "(1) Which part of my subconscious do you hale from?"
user2 = "(2) In a society dominated by the rights of capital, the past devours the future."
user3 = "(3) The less you know the more you beleive."
user4 = "(4) Populism is a word bankers use because they want to shift the blame."
output=f"{user1} \n{user2} \n{user3} \n{user4}"
print(output)
print()

# This example is from PA1 page 95. """ triple quotes isntead of \n.
unit_price = 49.95
quantity = 32
sales_tax_rate = 0.065
subtotal = quantity * unit_price
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax
output=f"""
Subtotal:  ${subtotal:,.2f}
Sales tax: ${sales_tax:,.2f}
Total:     ${total:,.2f}
"""
print(output)
print()
# Formatting width and alignment. page 96 PA1.  The > sign and the numnber move the $ sign 
unit_price = 49.95
quantity = 32
sales_tax_rate = 0.065
subtotal = quantity * unit_price
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax
output=f"""
Subtotal:  ${subtotal:>9,.2f}
Sales tax: ${sales_tax:>9,.2f}
Total:     ${total:>9,.2f}
"""
print(output)
print()
# Numerical values
unit_price = 49.95
quantity = 32
sales_tax_rate = 0.065
subtotal = quantity * unit_price
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax
# Format amounts to show as string with leading dollar sign
s_subtotal = "$" + f"{subtotal:,.2f}"
s_sales_tax = "$" + f"{sales_tax:,.2f}"
s_total = "$" + f"{total:,.2f}"

# Output the string with dollar sign already attached.This alligns all of it. 
output=f"""
Subtotal:   {s_subtotal:>9}
Sales tax:  {s_sales_tax:>9}
Total:      {s_total:>9}
"""
print(output)
# Lesson learned!  I fought the above code for half an hour before I 
# I figured out s_total was wrongly put in as s-total on line 126.
# But it told me the error was on line 127??   
# This was on page 97 of PA1.
