sentence : str = "Learning to code requires practice, patience, and problem solving skills"
word : str = "code"
print("The length of the sentence:", len(sentence))
print("The length of the sentence in words:", len(sentence.split()))
print("The index of the first occurrence of the word", sentence.index(word))
print("The number of times the word appears", sentence.count(word))
print("Uppercase letters:", sentence.upper())
print("Lowercase letters:", sentence.lower())
new_word = "program"
print("Replace the word in the sentence with a new word:",sentence.replace(word, new_word))
print("Last character of the sentence:", sentence[-1])