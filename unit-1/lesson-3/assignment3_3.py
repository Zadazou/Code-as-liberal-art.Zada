import sys
from PIL import Image

if len(sys.argv) != 3:
    exit("This command requires two argument: the name of two image files")

img1 = Image.open( sys.argv[1] )
img2 = Image.open( sys.argv[2] )

blended_img = Image.blend(img1,img2,0.5)
blended_img.save("Blended.jpg")