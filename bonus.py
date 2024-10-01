# Define a string variable containing a sentence with at least 10 words.
sentence = "Tuwaiq Academy offers top-notch training in technology and innovation."

# Define a string variable containing a word that appears in the sentence.
word = "Tuwaiq"

# Print the length of the sentence
print("Length of the sentence:", len(sentence))

# Print the index of the first occurrence of the word in the sentence
print("Index of the first occurrence of the word:", sentence.index(word))

# Print the number of times the word appears in the sentence
print("Number of times the word appears in the sentence:", sentence.count(word))

# Print the sentence in all uppercase letters
print("Sentence in uppercase:", sentence.upper())

# Print the sentence in all lowercase letters
print("Sentence in lowercase:", sentence.lower())

# Replace the word in the sentence with a new word of your choice
new_word = "SADAIA"
new_sentence = sentence.replace(word, new_word)
print("Sentence after replacing the word:", new_sentence)

# Print the last character of the sentence
print("Last character of the sentence:", sentence[-1])