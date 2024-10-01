sentence: str = "I like Python and for me coding in Python is fun"
language: str = "Python"

# Print the length of the sentence.
print(f"Length: {len(sentence)}")

# Print the index of the first occurrence of the word in the sentence.
print(f"Index of first occurence: {sentence.index(language)}")

# Print the number of times the word appears in the sentence.
print(f"Number of appearance: {sentence.count(language)}")

# Print the sentence in all uppercase letters.
print(f"In uppercase: {sentence.upper()}")

# Print the sentence in all lowercase letters.
print(f"In lowercase: {sentence.lower()}")

# Replace the word in the sentence with a new word of your choice.
print(f"Replace Python: {sentence.replace(language, 'Javascript')}")

# Print the last character of the sentence.
print(f"The last characeter: {sentence[-1]}")