phrase = "MD Amdadul Islam Dhrubo has the youtube channel DHRUBOISH"

# Making String Uppercase
print(phrase.upper())


# Making String LowerCase
print(phrase.lower())

# Checking whether it's lowercase or uppercase
print(phrase.isupper())
# It will be true if all of the alphabet of phrase are in upperCase
print(phrase.islower())
# It will be true if all of the alphabet of phrase are in lowerCase


# Making all uppercase and then checking
print(phrase.upper().isupper())

# Making all lowercase and then checking
print(phrase.lower().islower())


# Length of a string; "len" keyword will say the number of character in a string.
print(len(phrase))


# Get a particular character of string
print(phrase[0])


# Get the position of a specific character 
# Use of index() function in python
print(phrase.index("D"))
# Remember it will always give the first position of 'D'. If you have multiple "D" .


# Get the position of more than one character
print(phrase.index("DHRUBOISH"))
# Remember it will give the starting position of the characters "DHRUBOISH"



# Replace() fucntion
# Replace word or character by another
print(phrase.replace("DHRUBOISH", "Dhruboish Youtube"))
# Here 1st string inside the replace() function is the word you want to change and the last one is the word by which you want to change.