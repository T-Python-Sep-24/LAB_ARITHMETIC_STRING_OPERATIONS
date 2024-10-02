Price=2.99  
Quantity=3
Tax_rate=7.5/100    #converting it to decimal

Subtotal=round(Price*Quantity,2)
Tax=round(Subtotal*Tax_rate,2)
Total=round(Subtotal+Tax,2)

print(f"\nPrice of item: ${Price}")
print(f"Quantity: {Quantity}")
print(f"Tax rate: {Tax_rate*100}%\n")
print(f"Subtotal: ${Subtotal}")
print(f"Tax: ${Tax}")
print(f"Total: ${Total}")
