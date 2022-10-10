programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

# Retrieving Bug from dictionary
#print(programming_dictionary["Bug"])

# Adding new items to the dictionary
programming_dictionary["Parameter"] = "a value passed into a function"

#print(programming_dictionary)

# Create an empty dictionary
empty_dictionary = {}
#print(empty_dictionary)

# Wipe an existing dictionary
#programming_dictionary = {}
#print(programming_dictionary)

# Edit an existing item in the dictionary
programming_dictionary["Parameter"] = "A value passed into a function, which can take in an argument when the function is called"
#print(programming_dictionary)

# Loop through a dictionary

for item in programming_dictionary:
    print(item)
    print(programming_dictionary[item])


