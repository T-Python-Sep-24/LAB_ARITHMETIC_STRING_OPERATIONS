#Defining a String with at least 10 words
someSentence = "It is international coffee day, and the price of a coffee cup was 1SR"

#Defining a String with a single word from the sentence
word = "coffee"

#The original sentence
print(someSentence)

#Length of the sentence
print(f"Number of characters in the sentence is: {len(someSentence)}")

#The number of times the word "coffee" appeared in the sentence
print(f"Number of times the word {word} appeared in the sentence is: {someSentence.count(word)}")

#Sentence in upper case
print(f"The sentence to upper case: {someSentence.upper()}")

#Sentence in lower case
print(f"The sentence to lower case: {someSentence.lower()}")

#Replace the word "coffee" with "mojito" 
print(f"The sentence after replacing '{word}' with 'mojito': {someSentence.replace(word, "mojito")}")

#Last character in the sentence
print(f"Last character in the sentence is: {someSentence[-1]}")