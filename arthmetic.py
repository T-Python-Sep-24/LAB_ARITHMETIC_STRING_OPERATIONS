# Define variables
price = 2.99  # cost of the item
quantity = 3  # number of items
tax_rate = 0.075  # tax rate in decimal form (7.5%)

# Calculating the subtotal
subtotal = price * quantity

# Calculating the tax
tax = subtotal * tax_rate

# Calculating the total cost
total = subtotal + tax

# Print results formatted as currency
print(f"Price of item: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Tax rate: {tax_rate * 100:.1f}%\n")

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")