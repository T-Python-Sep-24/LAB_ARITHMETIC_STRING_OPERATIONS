price = 2.99
quantity= 3
tax_rate= 7.5
subtotal = price * quantity
tax = (tax_rate/100) * subtotal
total= subtotal + tax

result="price of item: ${:.2f}\nQuantity: {}\nTax rate: {}%\n\nSubtotal: ${:.2f}\nTax: ${:.2f}\nTotal: ${:.2f}".format(price,quantity,tax_rate,subtotal,tax,total)
print(result)