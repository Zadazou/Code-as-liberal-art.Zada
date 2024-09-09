# import sys

# data = [ 643, 452, 230, 219, 962, 532 ]

# index = int(sys.argv[1])

# print( data[index] )


import sys
from PIL import Image

img = Image.open( sys.argv[1] )

print("You typed the filename: " + sys.argv[1] )
print("This is a " + img.format)
print(img.format_description)
print("Size: " + str(img.size) )