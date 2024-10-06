import sys
from PIL import Image 

# # if len(sys.argv) != 3:
# #     exit("This program requires two arguments: the name of two image files to combine.")


# # open both images
# img1 = Image.open( sys.argv[1] ).convert('RGBA')
# img2 = Image.open( sys.argv[2] ).convert('RGBA')


# # resize both images so they are no bigger than 400x400
# # but preserve the original aspect ratio
# img1.resize( (400,400) )
# img2.resize( (400,400) )

# # make a new image 600x600, with a white background
# # Note that this image now has an "alpha" component
# new_image = Image.new( "RGBA", (400,600), (0, 0, 0, 0) )

# # paste in the first image to the upper-left corner (0,0)
# new_image.paste(img1, (0,0) )

# # add some transparency (alpha) to the second image
# img2.putalpha(128)

# # paste in the second image, preserving its new transparency
# new_image.paste(img2, (20,0) )

# # save the resulting image
# # Note that we must convert it to RGB with no alpha to save it as a JPEG
# new_image.convert("RGB").save("blank1.jpg")

# # Alternatively, we could have avoided converting by saving it to a
# # PNG like this (since PNGs allow alpha):
# # new_image.save("overlay-transparent.png")

img1 = Image.open( sys.argv[1] ).convert("RGBA")
img2 = Image.open( sys.argv[2] ).convert("RGBA")
img2 = img2.resize(img1.size)
img3 = Image.alpha_composite(img1, img2)
img3.convert("RGB")
img3.save("pngmix.png")