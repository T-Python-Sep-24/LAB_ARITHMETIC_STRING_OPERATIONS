price = 2.99
quantity = 3
tax_rate = 7.5

subtotal = price * quantity
tax = subtotal * (tax_rate / 100)

total = subtotal + tax

print(f'Price of item: SAR {price}')
print('Quantity: ', quantity)
print(f'Tax rate: {tax_rate}%')
print('')
print(f'Subtotal: SAR {subtotal}')
print(f'Tax: SAR {round(tax, 2)}')
print(f'Total: SAR {round(total, 2)}')