import sys
from PIL import Image, ImageDraw, ImageFilter
import random
from os import listdir, path

files = listdir(sys.argv[1])
#Opens the folder that is typed in terminal
random_file1 = random.choice(files)
random_file2 = random.choice(files)
#Opends two random images from the folder
img1 = Image.open( path.join(sys.argv[1],random_file1) )
img2 = Image.open( path.join(sys.argv[1],random_file2) )

#1. The first images is going to be converted in to black and white by making pixels close to white completely white and the others black.
#2. The black pixels of the image is going to turn into a random color and this image is saved as a seperate image
#3. The white pixels is going to be changed into another random color. And on top there will be 1000 randomly places opposite-colored speckles. saved as a seperate image
#4. The seperately colored black and white part of the image overlays ontop of each other to create a new colored image
#5. Make an ellipse shaped mask layer with Image.draw in the middle of the frame.
#6. Use the second randomly choosed image as the base layer and paste the new colored image from step4 on top with the ellipse mask.
#7. Final outcome. the second radomly choosed image appears in the ellips in the middle of the newly colored first randomly choosed image.


img3 = img1.copy()
img_hsv = img3.convert(mode="HSV")
img_hsv_data = img_hsv.getdata()

new_img_data = []
#get pixels that are close to white and turn these pixels completely white
for p in img_hsv_data:
    if p[2] > 90 and p[1] < 25: #any pixels brighter than 90 and less saturated than 25(approximate to white)
        new_img_data.append( (0,0,0) ) 

    else:
        new_img_data.append( (0, 0, 255) )

img_hsv.putdata(new_img_data)
# put changed pixels back in to the image
img_rgb = img_hsv.convert("RGB")
img_rgb.save("first.jpg")
newp1 = img_rgb.resize( (400, 400) )
# convert the image back to RGB mode and into the wanted size for next step
rgbdata = newp1.getdata()
#set three random numbers for RGB color
r1 = int(random.random() * 255 )
r2 = int(random.random() * 255 )
r3 = int(random.random() * 255 )
# set all the priviously turned-black pixels to the new random color
# now newp1 is the black and white image that has a random color replacing the black
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
#set three random numbers for RGB color
n1 = int(random.random() * 255 )
n2 = int(random.random() * 255 )
n3 = int(random.random() * 255 )
white = newp2.getdata()
wdata = []
for w in white:
    if w[0] != 0 and w[1] != 0 and w[2] != 255:#geting  all the none white pixels
        wdata.append((255, 255, 255, 0))#turn transparent
    else:
        wdata.append((n1, n2, n3, 255))
        #make all the none white pixels transparent and the white pixles into the new random color
newp2.putdata(wdata)
# set three new random dunmbers to make the opposite of the last random color
s1 = 255 - n1
s2 = 255 - n2
s3 = 255 - n3
# making 1000 random speckles on the newp2 image 
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
# the newly colored white part and black part lay ontop of each other and make a new colored image
image3.convert("RGB")
image3.save("mix.jpg")

# Make an ellipse shaped mask layer with Image.draw in the middle of the frame.
mask_img = Image.new("L", (400, 400), 255)
draw = ImageDraw.Draw(mask_img)
draw.ellipse((150, 100, 250, 300), fill=0)
mask_im_blur = mask_img.filter(ImageFilter.GaussianBlur(10))
mask_im_blur.save("mask.jpg")
# making 1000 random speckles on the second chosen image 
newimg2 = img2.resize( (400, 400) ).convert("RGBA")
for dot in range(1000):
    x = int( random.gauss(200, 60) ) % 400
    y = int( random.gauss(200, 60) ) % 400
    newimg2.putpixel( (x,y), (s1, s2, s3, 255) )
# Make the second radomly choosed image appears in the ellips in the middle of the newly colored first randomly choosed image
back_img = newimg2.copy()
back_img.paste(image3, (0,0), mask_im_blur)
back_img.save("collage" + str(n3) + ".jpg") #use the randomly generated number to mane the outcome

