#define Prices
itemPrices = {
    "apple": 10,
    "water": 2.5,
    "coffee": 11,
    "bread": 1.99
}

#user input for the item and quantity
item = input("Enter the item : ")
if item in itemPrices:
    quantity = int(input("Enter the quantity : ")) #(step 2)
    
    #define a variable named "price" (step 1)
    price = itemPrices[item]
    
    #define the tax rate (step 3)
    tax_rate = 10

    #calculate the subtotal (step 4)
    subtotal = price * quantity

    #calculate the tax (step 5)
    tax = subtotal * 0.1

    #calculate the total  (step 6)
    total = subtotal + tax

    # Print (step 7)
  
    bill= "\n Item : {} \n Price of item : {}$ \n Quantity : {} \n Tax rate : {}% \n \n Subtotal : {}$ \n Tax : {} \n Total : {} ".format(
        item,price,quantity,tax_rate,subtotal,tax,total)
    print(bill)
else:
    print("Sorry, that item is not available")
