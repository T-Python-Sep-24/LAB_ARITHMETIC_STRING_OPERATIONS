
price = 2.99
quantity = 3
tax_rate = 0.075

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print("Price of item:  $", round(price, 2))
print("Quantity:  ", quantity)
print("Tax rate:  ", round(tax_rate * 100, 1))
print()
print("Subtotal: $",round(subtotal, 2))
print("Tax: $",round(tax, 2))
print("Total: $",round(total, 2))