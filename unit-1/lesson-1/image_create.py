
from PIL import Image

# Print a blank line
print("\n")

# Prompt the user for some info
name = input("Please enter a filename: ")
size = int(input("Type a number between 10 and 1000: "))
color = input("Type any color: ")

img = Image.new("RGB",(size,size),color)
img.save(name + ".png")

#when I run the code, I got "ModuleNotFoundError: No module named 'PIL'".
#  Does it mean I don't have the python image library?