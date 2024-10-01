price=float(2.99)
quantity=int(3)
taxRate=0.075
subtotal=price*quantity
tax= subtotal*taxRate
total= tax + subtotal
print(f"subtotal:${subtotal}\n"
      f"tax;${round(tax, 2)}\n"
      f"total cost:${round(total, 2)}")
