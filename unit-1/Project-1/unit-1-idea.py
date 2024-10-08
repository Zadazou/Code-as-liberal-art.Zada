## gennerate pixels from scratch. 
#  From PIL import Image
# import random

# set coorninates for the pixels.
# use random.gausse & randrange to restran the range of the modified pixels
# use code in classnote-5 exercise 7 to generate the different shade random pixels
# use code in classnote-4 to create gradian patterns
#overlay them together to create new image
#in the overlay either select some of the pixels to make them transparent, or use alpa composite to overlay half transparent images together.

# using existing images to collage
# import system
# from os import listdir, path 
# create a folder of images that I whant to use
# create a new images backgrond through genreating pixels 400*400
# use random command to choose images form the folder
# create Filter to modify the images
# apply rotaions
# then overlay the filtered images on to the background 
import sys
from PIL import Image, ImageDraw, ImageFilter

# if len(sys.argv) != 3:
#     exit("This command requires two argument: the name of two image files")

# mask_img = Image.new("L", (400, 400), 255)
# draw = ImageDraw.Draw(mask_img)
# draw.ellipse((150, 100, 250, 300), fill=0)
# mask_im_blur = mask_img.filter(ImageFilter.GaussianBlur(10))
# mask_im_blur.save("mask.jpg")

# img1 = Image.open( sys.argv[1] )
img2 = Image.open( sys.argv[2] )

# # attempting to selesct white pixels in picture and turn then transparent
img3 = img2.copy()
img_hsv = img3.convert(mode="HSV")
img_hsv_data = img_hsv.getdata()

new_img_data = []
#get pixels that are close to white 
# and turn these pixels completely white
for p in img_hsv_data:
    if p[2] > 90 and p[1] < 10: #any pixels brighter than 90 and less saturated than 10(approximate to white)
        new_img_data.append( (0,0,0) ) 
    else:
        new_img_data.append( (0, 0, 255) )

img_hsv.putdata(new_img_data)
img_rgb = img_hsv.convert("RGB")
# mask = img_rgb.convert("RGBA")
mask = img_rgb.resize( (400, 400) )
# mask.save("mask.jpg")
draw = ImageDraw.Draw(mask)
draw.ellipse((150, 100, 250, 300), fill=0)
# mask_im_blur = mask.filter(ImageFilter.GaussianBlur(10))
mask.convert("RGBA")
mask.save("newmask.png")
# # # apply alpha channel allowing transparency
# datas = newimage2.getdata()

# newData = []
# for item in datas: # get all white pixles and turn them transparent
#     if item[0] == 255 and item[1] == 255 and item[2] == 255:
#         newData.append((255, 255, 255, 0))
#     else:
#         newData.append(item)

# newimage2.putdata(newData)
# newimage2.save("transparent.png", "PNG")

# newimage1 = img1.resize( (400, 400) ).convert("RGBA")
# newimage2 = img2.resize( (400, 400) ).convert("RGBA")

# back_img = newimage1.copy()
# back_img.paste(newimage2, (0,0), mask_im_blur)
# back_img.save("collage_4.jpg")




# blended_img = Image.blend(newimage1,newimage2,0.7)
# blended_img.save("try2.jpg")