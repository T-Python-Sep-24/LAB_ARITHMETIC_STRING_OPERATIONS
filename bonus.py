#Define a string variable containing a sentence with at least 10 words.
sentence = "My name is Hessa ALmasaad and I love coding."

#Define a string variable containing a word that appears in the sentence.
word = "coding"

#Print the length of the sentence.
print("Length of the sentence:",len(sentence))

#Print the index of the first occurrence of the word in the sentence.
index = sentence.find(word)
print(f"The index of the first occurrence of '{word}' in the sentence is: {index}")

#Print the number of times the word appears in the sentence.
count = sentence.lower().count(word.lower())
print(f"The word '{word}' appears {count} times in the sentence.")

#Print the sentence in all uppercase letters.
print(sentence.upper())

#Print the sentence in all lowercase letters.
print(sentence.lower())

#Replace the word in the sentence with a new word of your choice.
new_word = "programming"
new_sentence = sentence.replace(word, new_word)
print("The Original Sentence:", sentence)
print("The New Sentence:", new_sentence)

#Print the last character of the sentence.
last_character = sentence[-1]
print("The last character of the sentence is ",last_character)








