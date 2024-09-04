
# Print a blank line
print("\n")

# Prompt the user for their info
name = input("Please enter a name: ")
title = input("Please enter a title: ")
phone = input("Please enter a phone number: ")
address = input("Please enter an address: ")

file = open("newcard.txt","w")
file.write(name + "\n")
file.write(title + "\n")
file.write(phone + "\n")
file.write(address + "\n")

file.close()

