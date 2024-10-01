price = 2.99
quantity = 3
tax_rate = 0.075
rounded_tax=round(tax_rate,2)
subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax
print(f"Price of item:: ${price:.2f}")
print("Quantity:",quantity)
print(f"Tax rate: {tax_rate * 100:.1f}%")
print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
