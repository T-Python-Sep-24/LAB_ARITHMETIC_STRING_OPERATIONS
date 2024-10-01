# calculate the total cost of a customer's purchase, including tax.
price: float = 2.99
quantity: int = 3
tax_rate: float = 7.5    # the value in percentage

# calculate the subtotal
subtotal: float = price * quantity

# calculate the tax
tax: float = subtotal * (7.5 / 100)

# calculate the total cost
total = subtotal + tax


# Print the subtotal, tax, and total costs, formatted as currency
print(f"Price of item: ${price}")
print(f"Quantity: {quantity}")
print(f"Tax rate: {tax_rate}%\n")

print(f"Subtotal: ${subtotal}")
print(f"Tax: ${round(tax, 2)}")
print(f"Total: ${round(total, 2)}")