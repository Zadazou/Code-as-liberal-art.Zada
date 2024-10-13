# import sys
# from PIL import Image

# # Part 1 creating patterns. 
# if len(sys.argv) != 2:
#     exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 400x400 image
# img = Image.new("RGB", (400,400) )

# for y in range(400):
# # restraining the patterns to be in the middle of the image
#     for x in range(400):
#         if 326 > y > 72:
#             pixel = (x % 255, x-7+20 % 255, 255-y % 255)
# # making the bottom part 
#         if y > 326:
#             pixel = (34,78,12)
# # making the bottom part
#         if y < 72:
#             pixel = (157,72,24)

#         img.putpixel( (x,y), pixel )

# img.save(sys.argv[1])


# # Second variation of pattern creating
# if len(sys.argv) != 2:
#     exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 400x400 image
# img = Image.new("RGB", (400,400) )

# for y in range(400):

#     for x in range(400):

#         r = 255
#         g = 145
#         b = 56
# # making the base color orange
#         if x % 20 > 40:
#             r = x+30 % 255
#             g = 230-x % 255

#         if y % 20 > 40:
#             b = y+30 % 255
#             r = 230-y % 255

#         if x % 80 > 40 and y % 80 > 40:
#         #"if x % 100 > 50 and y % 100 > 50:" gets wider orange stripes
#             g = x+y+5 % 255
#             b = 355-x+y % 255


#         pixel = (r, g, b)
#         img.putpixel( (x,y), pixel )

# img.save(sys.argv[1])


# Part 2 Combining images

# if len(sys.argv) != 5:
#     exit("This program requires 4 arguments: the name of 4 image files to combine.")


# #open both images
# img1 = Image.open( sys.argv[1] ).convert("RGBA")
# img2 = Image.open( sys.argv[2] ).convert("RGBA")
# img3 = Image.open( sys.argv[3] ).convert("RGBA")
# img4 = Image.open( sys.argv[4] ).convert("RGBA")

# # resize both images so they are no bigger than 400x400
# # but preserve the original aspect ratio
# img1.thumbnail( (200,400) )
# img2.thumbnail( (200,400) )
# img3.thumbnail( (200,400) )
# img4.thumbnail( (200,400) )

# # make a new image 600x600, with a white background
# new_image = Image.new( "RGB", (400,400), "white" )

# # blend first two images
# blended_img1 = Image.blend(img1,img2,0.5)
# blended_img1.convert("RGB")

# # blend the other two images
# blended_img2 = Image.alpha_composite(img3,img4)
# blended_img2.convert("RGB")
# # paste in the first blended image to the upper-left corner (0,0)
# new_image.paste(blended_img1, (0,0) )

# # paste in the second blended image next to the forst imag (200,0)
# new_image.paste(blended_img2, (200,0) )

# # save the resulting image
# new_image.save("blended1+2.jpg")



# # # Attempting to selesct white pixels in picture and turn then transparent
# img = Image.open( sys.argv[1] )
# img_hsv = img.convert(mode="HSV")
# img_hsv_data = img_hsv.getdata()

# new_img_data = []
# #get pixels that are close to white 
# # and turn these pixels completely white
# for p in img_hsv_data:
#     if p[2] > 90 and p[1] < 10: #any pixels brighter than 90 and less saturated than 10(approximate to white)
#         new_img_data.append( (0,0,255) ) 
#     else:
#         new_img_data.append(p)

# img_hsv.putdata(new_img_data)
# img_rgb = img_hsv.convert("RGB")
# img = img_rgb.convert("RGBA")
# # # apply alpha channel allowing transparency
# datas = img.getdata()

# newData = []
# for item in datas: # get all white pixles and turn them transparent
#     if item[0] == 255 and item[1] == 255 and item[2] == 255:
#         newData.append((255, 255, 255, 0))
#     else:
#         newData.append(item)

# img.putdata(newData)
# img.save("transparent.png", "PNG")



