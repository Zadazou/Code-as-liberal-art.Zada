
# Print a blank line
print("\n")

# Ask the user for a filename
filename = input("Please enter the name of a file in this directory: ")

# Open that file
file = open(filename)

print("Name is: " + file.readline())
print("Title is: " + file.readline())
print("Phone number is: " + file.readline())
print("Address is: " + file.readline())

#I tried several names but they all came out "FileNotFoundError"