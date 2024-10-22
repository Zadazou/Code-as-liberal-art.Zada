from os import listdir, path
from PIL import Image, ExifTags

files = listdir("images")
img = Image.open(path.join("images", "collage1.jpg"))
exifData = img.getexif()
print(img)
print(exifData)
for key in img.getexif().keys():
    print(key, ExifTags.TAGS[key])