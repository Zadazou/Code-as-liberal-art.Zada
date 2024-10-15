import sys
from PIL import Image, ImageDraw, ImageFilter
import random
from os import listdir, path


files = listdir( sys.argv[1] ) 
#Opens the folder that is typed in terminal
random_file1 = random.choice(files)
random_file2 = random.choice(files)
#Opends two random images from the folder

img1 = Image.open( path.join(sys.argv[1],random_file1) )
img2 = Image.open( path.join(sys.argv[1],random_file2) )
#name the two images as img1 & img2

#1. The first images is going to be converted in to black and white by making pixels close to white completely white and the others black. save as a 400*400 image
#2. The black pixels of the image is going to turn into a random color and this image is saved as a seperate 400*400 image
#3. The white pixels is going to be changed into another random color. And on top there will be 1000 randomly places opposite-colored speckles. saved as a seperate 400*400 image
#4. The seperately colored black and white part of the image overlays ontop of each other to create a new colored image. save as a 400*400 image
#5. Get all the close to white pixels of the second chosen image and turns them in to a seperate random color and add speckles.save as a 400*400 image
#6. Make a background canvas of 800*800 pixels
#6. Final result: Put the image from step 1 on the top left corner of the canvas, the image from step3 on the top right corner, the image form step 4 on the bottom left corner, and the image from step 5 on the bottom right corner


#Convert first image in to HSV mode
img3 = img1.copy()
img_hsv = img3.convert(mode="HSV")
img_hsv_data = img_hsv.getdata()

new_img_data = []
#get pixels that are close to white and turn these pixels completely white, and turn others black
for p in img_hsv_data:
    if p[2] > 90 and p[1] < 25: #any pixels brighter than 90 and less saturated than 25(approximate to white)
        new_img_data.append( (0,0,0) ) 

    else:
        new_img_data.append( (0, 0, 255) )

img_hsv.putdata(new_img_data)
# put changed pixels back in to the image
img_rgb = img_hsv.convert("RGB")
newp1 = img_rgb.resize( (400, 400) )
left1 = newp1.copy()
# convert the image back to RGB mode and into the wanted size for next step
newp1.save("first.jpg")
# save the first step outcome which is a black and white image of the first random image choosen

rgbdata = newp1.getdata()
#set three random numbers for RGB color
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
# set all the priviously turned-black pixels to the new random color
# now newp1 is the black and white image that has a random color replacing the black

newpa = newp1.copy()
# copy the image to create a new layer
newp2 = newpa.convert("RGBA")
#set three random numbers for RGB color
n1 = int(random.random() * 255 )
n2 = int(random.random() * 255 )
n3 = int(random.random() * 255 )
#make all the none white pixels transparent and the white pixles into the new random color
white = newp2.getdata()
wdata = []
for w in white:
    if w[0] != 0 and w[1] != 0 and w[2] != 255: #geting  all the none white pixels
        wdata.append((255, 255, 255, 0)) #turn transparent
    else:
        wdata.append((n1, n2, n3, 255)) # turn new random color
newp2.putdata(wdata)
#newp2 is a image with only the white parts that's just colored and no black parts

# set three new random dunmbers to make the opposite of the last random color
s1 = 255 - n1
s2 = 255 - n2
s3 = 255 - n3
# making 1000 random speckles on the newp2 image 
for dot in range(1000):
    x = int( random.gauss(200, 60) ) % 400 # add "% 400" to make sure the random cooridinates don't go out of the frame which was an error I encountered
    y = int( random.gauss(200, 60) ) % 400
    newp2.putpixel( (x,y), (s1, s2, s3, 255) )
newp2.save("object.png")
# now newp2 is a image with colored object and opposite colored speckles

newp1.convert("RGBA")
newp1.save("back.png")
image1 = Image.open("back.png").convert("RGBA")
image2 = Image.open("object.png").convert("RGBA")
image3 = Image.alpha_composite(image1, image2)
# the newly colored white part and black part lay ontop of each other and make a new colored image
image3.convert("RGB")
image3.save("mix.jpg")

nimg2 = img2.resize((400,400)).convert(mode="HSV")
#gets all the close to white pixels from the second chosen image and converts them into a random color
(width, height) = nimg2.size

for x in range(width):
    for y in range(height):
        p = nimg2.getpixel((x,y))
        if p[2] > 90 and p[1] < 25:
            nimg2.putpixel( (x,y), (n2,n3,n1) )
newimg_rgb = nimg2.convert(mode="RGB")  
# put 1300 random speckles in a nother random color on the image
for n in range(1300):

    x = random.randrange(135, 400)
    y = random.randrange(0, 400)
    r = n1
    g = n2
    b = n3

    newimg_rgb.putpixel( (x,y), (r, g, b) )


newimg_rgb.save(str(n1) + ".jpg")
#make a new background canvas that is 800*800 pixels and white
canvas = Image.new("RGBA", (800,800), (0,0,255,255) )

canvas.paste(left1.convert("RGBA"), (0,0) ) #paste the black and white of img1 on the top left corner
canvas.paste(newp2.convert("RGBA"), (0,400)) # paste the colored black part of img1 on the top right corner
canvas.paste(image3.convert("RGBA"), (400, 0))# paste the overlayed newly colored black and white part of img1 on the bottom left corner
canvas.paste(newimg_rgb, (400, 400)) # paste the newly colored img2 on the bottom right corner.
canvas.save("Final" + str(n2) + ".png") #use the randomly generated number to mane the outcome