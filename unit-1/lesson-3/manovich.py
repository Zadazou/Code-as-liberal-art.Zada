# 1. NUMERICAL REPRESENTATION

# “All new media objects, whether created from scratch on
# computers or converted from analog media sources, are
# composed of digital code; they are numerical
# representations.”


from PIL import Image

image = Image.open("Z.jpg")

for w in range(image.size[0]):
    for h in range(image.size[1]):
        if h % 2 == 0 and w > 300:
            image.putpixel((w, h), (255, 0, 4))
image.save("2.jpg")







# 2. MODULARITY

# “the fractal structure of new media” (Manovich, 30)

# “Elements are assembled into larger-scale objects but
# continue to maintain their separate identities.” (ibid)

# from PIL import Image

# def glitchImageWithRed(imageFile, color, uniqueFileName):
#     image = Image.open(imageFile)

#     for w in range(image.size[0]):
#         for h in range(image.size[1]):
#             if h % 2 == 0 and w > 300:
#                 image.putpixel((w, h), color)
#     image.save("new-image-" + uniqueFileName + ".jpg")


# glitchImageWithRed('image-1.jpg', (123,0,0), "rando")



# 3. AUTOMATION

# “Human intentionality can be removed from the creative
# process, at least in part.” (Manovich, 32)

# Agree?? Disagree? What is an example from your work so far?





# 4. VARIABILITY

# “A new media object is not something fixed once and for
# all, but something that can exist in different, potentially
# infinite versions.” (Manovich, 36)

# “Instead of identical copies, a new media object typically
# gives rise to many different versions.”

# What can we say about this new/old dyad that Manovich is trying to disrupt?







# 5. TRANSCODING

# “New media can be thought of as consisting of two distinct
# layers — the cultural layer & the computer layer.” (46)

# transcode in a more literal sense: “to translate something
# into another format” (47)

# “The computerization of culture gradually accomplishes
# similar transcoding in relation to all cultural categories and
# concepts.” (47)

## What does he mean the computerization of culture? Can culture be computed? What does the process of transcoding assume about the ability to translate from one format to another format?


# Extra
# What did you think about his writing on interactivity?

## CLASSWORK
# Make a ManovichBot

# Work with a partner

# Create a new file called manovich-bot.py
# import the sys library at the top of your file


# create another new file called manovichdata.py
# this will be your text data file
# create 5 empty list objects for each Manovich principle
# populate each one with two or three sentences about that principle, you can be creative with your words here and refer to our discussion and reading response doc!
# for example one list object would look like this:

# variability = ["A new media object is not a static thing with a singular meaning or representation.", "Is anything ever really new?", "New media is about versions not about originality."]




# once you have these written, go back to your manovich-bot.py
# import all of the data from manovichdata.py, remember the * symbol stands for everything in the file

# write a for loop for one of your list objects, for example:

# for v in variability:
#   print(v)

# this is just to make sure that you can access your data and write code to do stuff with it

# now, for each Manovich principle, the user of your program should be able to run a command like this:

# python3 manovich-bot.py variability 

#  and the program should return to your user one of the sentences from your Manovich data set...

# repeat this for the other four principles! be creative with how you produce your output! you can also experiment with retrieving different kinds of input using sys.argv (remember this from lesson 3 notes)

# extra! can you add error handling is the user writes a typo? can you turn some of the code into a function that can be reused for each of the 5 principle?
