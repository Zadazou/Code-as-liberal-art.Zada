from PIL import Image
import random


# ## pixel grid!
# imagePixels = [];
# width = 100
# height = 100
# for y in range(100):
#     for x in range(100): 
#         imagePixels.append((x,y))

# print(imagePixels, "\n \n \n There are", len(imagePixels), "pixels because the width multiplied by the height", width, "x", height, "is equal to", width*height)





## 3
# let's make a 100x100 black image

# width = 100
# height = 100

# img = Image.new("HSV", (width,height), (0,0,0) )

# for y in range(height):
#     for x in range(width):    
#         # randomColorValue = random.randrange(255)
    
#         r = random.random()

#         if r > .9:
#             img.putpixel( (x,y), (240,255,255) )

# img = img.convert("RGB")

# randomnumforimg = int(random.random() * 10)

# img.save("so-less-random" + str(randomnumforimg) + ".png")





# #### 4


# #### let's make a 100x100 white image

width = 100
height = 100

img = Image.new("RGB", (width,height), (255,255,255) )

# loop 500 times, and each time, pick a random x and a random y
# and draw a pixel there
for n in range(500):
    
    ## even distribution
    # x = int( random.random() * 100 )
    # y = int( random.random() * 100 )

    # ## gaussian distribution
    # x = int( random.gauss(50,10) )
    # y = int( random.gauss(50,10) )

    # # gaussian distribution just for x
    # x = int( random.gauss(50,10) )
    # y = int( random.random() * 100  )

    r = int( random.gauss(50,10) )
    r**2 = x**2 + y**2

    img.putpixel( (x,y), (0,0,0) )

img.save("more-rando-gauss-x.png")







# #5
# lyric = ['i','write','poems','on','my','computer']
# # random.seed(2)
# i = random.randrange( len(lyric) ) 
# aRandomWord = lyric[i]

# # aRandomWord = random.choice(lyric)

# print(aRandomWord)





## 6 in class exercise

# from os import listdir, path
# import random
# from PIL import Image

# files = listdir("images")
# # files.remove(".DS_Store")

# random_file = random.choice(files)

# img = Image.open( path.join("images",random_file) )

# print(img)
# img.save("picked.jpg")



# ### 7
# ##let's make a 100x100 white image

# width = 100
# height = 100

# img = Image.new("HSV", (width,height), (0,0,255) )

# # ##loop 500 times, and each time, pick a random x and a random y
# # ## and draw a pixel there
# for n in range(500):

#     x = int( random.gauss(50,10) )
#     y = int( random.gauss(50,10) )

#     h = random.randrange(155,185)
#     s = random.randrange(235,255)
#     v = random.randrange(100,255)

#     img.putpixel( (x,y), (h,s,v) )

# img = img.convert(mode="RGB")
# img.save("rando-final.png")


