# import sys

# print( sys.argv )

# print( len(sys.argv) )

import sys

data = [ 643, 452, 230, 219, 962, 532 ]

index = int(sys.argv[1])
if len(sys.argv) < 2:
    print("You forgot to type an argument")
    exit()
if index >= len(data):
    print("You typed a number that's too large")
    exit()

print( data[index] )