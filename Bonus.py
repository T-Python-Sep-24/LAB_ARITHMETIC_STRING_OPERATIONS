Str1="I want to make a sentence that contain at least ten words"
Str2="contain"
print(f"The length is : {len(Str1)}")
print(f"First occurrence: {Str1.index(Str2)}")
print(f"Appearance: {Str1.count(Str2)}")
print(f"LowerCase: {Str1.lower()}")
print(f"UpperCase: {Str1.upper()}")
print(f'Replace The world "Count": {Str1.replace(Str2,"has")}')
print(f"Last index: {Str1[-1]}")