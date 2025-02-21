stringexample  = "Hello, World!"
listexample = ["Eggs", "Bacon", "Cheese", "Milk", "Bread"]

print(stringexample[0]) # We can call a specific item inside stringexample, in this case the first character
print(listexample[3]) # We can do the same for a list
print(len(stringexample)) # We can also check the length of a string
print(len(listexample)) # We can also check the length of a list

#We see that they are very similar, as python allows common operations between them. This includes the following:
reversestring = stringexample[::-1] # We can reverse a string
reverselist = listexample[::-1] # We can reverse a list
print(reversestring)
print(reverselist)

#The main difference begins when we try to change parts of it

try:
    stringexample[0] = "J" # This will give an error, as strings are immutable
except TypeError:
    print("Error changing string")

try:
    listexample[0] = "Spinach" # This will work, as lists are mutable
    print(listexample)
except TypeError:
    print("Error changing list")

# In order to achieve a similar effect with strings, we can slice them instead.
stringexample = "J" + stringexample[1:] # This will change the first character of the string
print(stringexample)
