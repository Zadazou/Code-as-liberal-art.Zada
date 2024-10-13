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
import random
# import collections
# from os import listdir, path
## if len(sys.argv) != 3:
##     exit("This command requires two argument: the name of two image files")

## mask_img = Image.new("L", (400, 400), 255)
## draw = ImageDraw.Draw(mask_img)
## draw.ellipse((150, 100, 250, 300), fill=0)
## mask_im_blur = mask_img.filter(ImageFilter.GaussianBlur(10))
## mask_im_blur.save("mask.jpg")

# img1 = Image.open( sys.argv[1] )
img2 = Image.open( sys.argv[1] )

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
img_rgb.save("first.jpg")
# mask = img_rgb.convert("RGBA")
newp1 = img_rgb.resize( (400, 400) )
rgbdata = newp1.getdata()

r1 = int(random.random() * 255 )
r2 = int(random.random() * 255 )
r3 = int(random.random() * 255 )
newdata = []
for p in rgbdata:
    if p[2] != 255:
        newdata.append((r1, r2, r3))
    else:
        newdata.append(p)
newp1.putdata(newdata)
newp1.save("newp1.jpg")
newpa = newp1.copy()
newp2 = newpa.convert("RGBA")
n1 = int(random.random() * 255 )
n2 = int(random.random() * 255 )
n3 = int(random.random() * 255 )
white = newp2.getdata()
wdata = []
for w in white:
    if w[0] != 0 and w[1] != 0 and w[2] != 255:
        wdata.append((255, 255, 255, 0))
    else:
        wdata.append((n1, n2, n3, 255))
newp2.putdata(wdata)
s1 = 255 - n1
s2 = 255 - n2
s3 = 255 - n3
for dot in range(1000):
    x = int( random.gauss(200, 60) ) % 400
    y = int( random.gauss(200, 60) ) % 400
    newp2.putpixel( (x,y), (s1, s2, s3, 255) )
newp2.save("object.png")

newp1.convert("RGBA")
newp1.save("back.png")
img1 = Image.open("back.png").convert("RGBA")
img2 = Image.open("object.png").convert("RGBA")
img3 = Image.alpha_composite(img1, img2)
img3.convert("RGB")
img3.save("mix.jpg")

mask_img = Image.new("L", (400, 400), 255)
draw = ImageDraw.Draw(mask_img)
draw.ellipse((150, 100, 250, 300), fill=0)
mask_im_blur = mask_img.filter(ImageFilter.GaussianBlur(10))
mask_im_blur.save("mask.jpg")
newimg2 = Image.open( sys.argv[2] ).resize( (400, 400) )

back_img = newimg2.copy()
back_img.paste(img3, (0,0), mask_im_blur)
back_img.save("collage.jpg")



# randomp = random.sample(background, 40)
# print(randomp)
# n1 = int(random.random() * 255 )
# n2 = int(random.random() * 255 )
# n3 = int(random.random() * 255 )
# randomp.append((n1, n2, n3))
# print(randomp)
# newp1.save("U1.jpg")

# for x, y, color in randomp:
#         newp1.putpixel((x, y), color)
# n1 = int(random.random() * 255 )
# n2 = int(random.random() * 255 )
# n3 = int(random.random() * 255 )

# newdata1 = random.sample(newdata, 100)

# newp1.putpixel(newdata1,(n1, n2, n3))
    
# newp1.save("U1.jpg")

# width, height = newp1.size
# coordinates = []
# for x in range(width):
#     for y in range(height):
#         if newp1.getpixel((x, y)) != (0, 0, 225):
#              coordinates.append((x, y))

# pixels = []
# for n in range (200):
#     x1 = int( random.gauss(50,40) )
#     y1 = int( random.gauss(50,40) )

# common_cord = set(coordinates).intersection(set(pixels))
# n1 = int(random.random() * 255 )
# n2 = int(random.random() * 255 )
# n3 = int(random.random() * 255 )
# common_cord = (n1, n2, n3)


    

# newp1.save(str(r1) + ".jpg")

# draw = ImageDraw.Draw(mask)
# draw.ellipse((150, 100, 250, 300), fill=0)
# # mask_im_blur = mask.filter(ImageFilter.GaussianBlur(10))
# mask.convert("RGBA")
# mask.save("newmask.png")
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