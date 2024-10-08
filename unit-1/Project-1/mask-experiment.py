import sys
from PIL import Image, ImageDraw, ImageFilter
img1 = Image.open( sys.argv[1] )
img2 = Image.open( sys.argv[2] )
img3 = Image.open( sys.argv[3] )

newimage1 = img1.resize( (400, 400) ).convert("RGBA")
newimage2 = img2.resize( (400, 400) ).convert("RGBA")
# newimage3 = img3.convert("RGBA")

#back_img = Image.new("RGBA", (400,400), (255,255,255))
back_img = newimage1.copy()
back_img.paste(newimage2, (0,0), img3)
back_img.save("MEN.png")


# mask_img = Image.new("L", (400, 400), 255)
# draw = ImageDraw.Draw(mask_img)
# draw.ellipse((150, 100, 250, 300), fill=0)
# mask_im_blur = mask_img.filter(ImageFilter.GaussianBlur(10))
# mask_im_blur.save("mask0.jpg")
