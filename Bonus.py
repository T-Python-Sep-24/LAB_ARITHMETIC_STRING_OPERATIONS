
sentence = "Last summer, we spent an unforgettable week at the beach, watching sunsets and we spent hours collecting beautiful seashells and enjoying the waves"
word ="spent"
print("\n length of the sentence : ",len(sentence))
print("first occurrence of the word in the sentence : ",sentence.lower().index(word))
print("the number of times the word appears in the sentence : ",sentence.lower().count(word))
print("all uppercase letters : ",sentence.upper())
print("all lowercase letters : ",sentence.lower())

newWord = "winter"
newSentence = sentence.replace("summer",newWord)
print(newSentence)

print("last character of the sentence : ", sentence[-1])






