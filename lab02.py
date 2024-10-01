from datetime import datetime
current_time = datetime.now()

print(" 1. coffee ($2.99) \n 2. tea ($1.22) \n 3. water ($0.55)")
choice = int(input("Enter Your Choice: "))

price = 0
if choice == 1:
    price = 2.99
elif choice == 2:
    price = 1.22
elif choice == 3:
    price = 0.55

quantity = int(input("Enter the quantity of the chosen product: "))

tax_rate = 7.5

subtotal = price * quantity # subtotal of products without taxes

tax = subtotal * (tax_rate / 100 ) # Tax

total = subtotal + tax # total of products and Taxes
print("-------------------- Receipt --------------------")
print(" Price of item: $", price, "\n Quantity: ", quantity, "\n Tax rate: ", tax_rate, "%")
print("\n Subtotal: $", subtotal, "\n Tax: $", tax, "\n Total $", total)
print("-----------",current_time.now(), "-----------")

