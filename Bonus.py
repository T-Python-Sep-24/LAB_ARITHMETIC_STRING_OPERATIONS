'''
- Define a string variable containing a sentence with at least 10 words.
- Define a string variable containing a word that appears in the sentence.
- Print the length of the sentence.
- Print the index of the first occurrence of the word in the sentence.
- Print the number of times the word appears in the sentence.
- Print the sentence in all uppercase letters.
- Print the sentence in all lowercase letters.
- Replace the word in the sentence with a new word of your choice.
- Print the last character of the sentence.
'''
Str1="I want to make a sentence that contain at least ten words"
Str2="contain"
print(len(Str1))
print(Str1.index(Str2))
print(Str1.count(Str2))
print(Str1.lower())
print(Str1.upper())
print(Str1.replace(Str2,"has"))
print(Str1[-1])