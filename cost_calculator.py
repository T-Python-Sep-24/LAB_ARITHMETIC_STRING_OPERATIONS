def calculate_total_cost(price, quantity, tax_rate):
    subtotal = price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax
    return subtotal, tax, total

def string_operations(code, word):
    length = len(code)
    first_index = code.index(word)
    count = code.count(word)
    upper_case = code.upper()
    lower_case = code.lower()
    new_sentence = code.replace(word, "phrase")
    last_char = code[-1]
    
    return length, first_index, count, upper_case, lower_case, new_sentence, last_char

# Part 1: 
price = 2.99
quantity = 3
tax_rate = 0.075

subtotal, tax, total = calculate_total_cost(price, quantity, tax_rate)

print(f"Price of item: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Tax rate: {tax_rate * 100:.1f}%\n")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
