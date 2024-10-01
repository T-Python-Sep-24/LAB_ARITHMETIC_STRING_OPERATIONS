#Lab 2

#informations

iteamPrice = 2.99
quantityNumber = 3
taxRate = 0.075


#Print 1

print(f"Price of item: ${iteamPrice:.2f}")
print(f"Quantity: {quantityNumber}")
print(f"Tax rate: ${taxRate * 100:.1f}%")


#Answers

Subtotal = iteamPrice * quantityNumber
Tax = Subtotal * taxRate
Total = Subtotal + Tax

#Print 2

print(f"Subtotal: ${Subtotal:.2f}")
print(f"Tax: ${Tax:.2f}")
print(f"Total: ${Total:.2f}")
