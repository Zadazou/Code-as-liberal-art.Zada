import sys
from PIL import Image

if len(sys.argv) != 2:
    exit("This command requires one argument: the name of an image file")
img = Image.open( sys.argv[1] )

print("You typed the filename: " + sys.argv[1] )
print("This is a " + img.format)
print(img.format_description)
print("Size: " + str(img.size) )