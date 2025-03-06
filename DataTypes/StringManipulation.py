str = "Learning Python"
print(str[0])
print(str[1])
print(str[2])
print(str[5])

modi = str.replace("Learning", "Earning through")
print(f"Original String: {str}\nModified String: {modi}")

print(str[0:]) # from 0 till end of string

print(str[0:6])  # till index 6 but it won't be included

print(str[6:])

print(str[-1]) # last character of string

print(f"Length of '{str}' is:",len(str))

sub_str = str[0:8]
print(sub_str)

str1 = str.lower()
str2 = str.upper()

print(str1)
print(str2)

print(f"The address of the string '{str1}' is",id(str1))
print(f"The address of the string '{str2}' is",id(str2))
print(f"The address of the character '{str1[0]}' is",id(str1[0]))
print(f"The address of the character '{str1[5]}' is",id(str1[5]))

s1 = "  Code    "
print(s1.strip()) # removes leading and trailing whitespaces by default
s2 = "==trip=="
print(s2.strip("=")) # removes mentioned leading and trailing symbol!
print(s2.lstrip("=")) # removes mentioned symbol from left side!
print(s2.rstrip("=")) # removes mentioned symbol from right side!

loc = str.find("Python") #find() is used to locate the given word in a string(by dfault it removes leading and trailing spaces)
print(f"The location of 'Python' in the string '{str}' is",loc)

str = 'Python is a versatile programming language'
# We Use the string.split() method to split the sentence into words and store it in a list
sp = str.split()

# here we are Using the "symbol".join() method to join words_list with a hyphen and store as a string
hyp = "-".join(sp)

# Print the list of words and the hyphenated sentence
print("List of words: ", sp)
print("Hyphenated sentence: " , hyp)
