price= 5
quantity= 4
tax_rate= 0.15
subtotal= price*quantity
tax= subtotal*tax_rate
total = subtotal + tax
desired_representation="Price of item : {} SAR \nQuantity : {} \nTax rate: {}%\nSubtotal:{} SAR \nTax: {} SAR \nTotal:{} SAR ".format(price, quantity ,tax_rate,subtotal , tax , total)
print(desired_representation)