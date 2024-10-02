#Defining cost of the item 
price = 7.77

#Defining the quantity of the item purchased
quantity = 7

#Defining tax rate
taxRate = 15

#Calculating the total price of items without the tax
subtotal = price * quantity

#Calculating the tax
tax = subtotal * (taxRate/100)

#Calculating final cost
total = subtotal + tax

#Printing the results 
print("Price of items:", price)
print("Quantity:", quantity)
print(f"Tax rate: {taxRate}%")
print("\nSubtotal:", subtotal)
print("Tax:", round(tax,2))
print("Total:", round(total,2))