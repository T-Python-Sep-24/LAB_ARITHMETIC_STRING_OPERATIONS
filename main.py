# assigning values
price = 2.99
quantity = 3
tax_rate = 0.075

# calculating 
subtotal = price*quantity
tax = subtotal*tax_rate
total = subtotal+tax


# print results
print("Price of item: ${}\nQuantity: {}\nTax rate: {}%\n".format(price,quantity,(tax_rate*100)))
print(f"\nSubtotal: ${subtotal}\nTax: ${round(tax,2)}\nTotal: ${round(total,2)}\n")
