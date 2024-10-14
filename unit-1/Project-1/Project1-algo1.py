import sys
from PIL import Image, ImageDraw, ImageFilter
import random
from os import listdir, path

files = listdir("Folder 1")
random_file1 = random.choice(files)
random_file2 = random.choice(files)

img1 = Image.open( path.join("Folder 1",random_file1) )
img2 = Image.open( path.join("Folder 1",random_file2) )

img3 = img1.copy()
img_hsv = img3.convert(mode="HSV")
img_hsv_data = img_hsv.getdata()

new_img_data = []
#get pixels that are close to white 
# and turn these pixels completely white
for p in img_hsv_data:
    if p[2] > 90 and p[1] < 25: #any pixels brighter than 90 and less saturated than 10(approximate to white)
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
image1 = Image.open("back.png").convert("RGBA")
image2 = Image.open("object.png").convert("RGBA")
image3 = Image.alpha_composite(image1, image2)
image3.convert("RGB")
image3.save("mix.jpg")

mask_img = Image.new("L", (400, 400), 255)
draw = ImageDraw.Draw(mask_img)
draw.ellipse((150, 100, 250, 300), fill=0)
mask_im_blur = mask_img.filter(ImageFilter.GaussianBlur(10))
mask_im_blur.save("mask.jpg")
newimg2 = img2.resize( (400, 400) ).convert("RGBA")
for dot in range(1000):
    x = int( random.gauss(200, 60) ) % 400
    y = int( random.gauss(200, 60) ) % 400
    newimg2.putpixel( (x,y), (s1, s2, s3, 255) )

back_img = newimg2.copy()
back_img.paste(image3, (0,0), mask_im_blur)
back_img.save("collage.jpg")

