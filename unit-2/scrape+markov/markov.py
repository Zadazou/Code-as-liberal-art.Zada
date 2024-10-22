import markovify

text = open("output.txt").read()

generator = markovify.Text(text)

paragraph = ""

for i in range(10):
    paragraph += str(generator.make_short_sentence(80))
    paragraph += " "

print("\n\n\n")
print(paragraph)
print("\n\n\n")


# Markovify returned:
#Return the meat to the drippings and butter. ALLRECIPES / KAREN HIBBARD Heat oil in a mixture of beef broth and red wine. Photos of Braised Beef Since this beef is braised along with any sides. Cover and place in the preheated oven until meat is very tender. Season and sear the beef broth and red wine. Season and sear the beef broth and red wine. I served it with any sides. Remove meat from the bottom. With over 20 years in the drippings and butter. Season and sear the beef broth and red wine. 
 
# This is really interesting. It's not a recipe but I see the potential. The text scraped from the website has a lot of information I didn't want, like text of the menu items and the drop-down options of the menu items. I think these items are the same for every recipe page from this website, so if I pop the lines of a certain amount it should remove all these unwanted information. The text now is a mixture of segments of cooking instructions and story of the dish, and it dosen't have list of the ingredients. I want to know if there is a way to seperate the text by titles. For example, separate the text from the recipe page into "ingredients" "cooking time" "cooking steps", then use marcovify to genrate text base on each section. 
# For unit 2 project, is it posible to make a recipe generator? Can I scrape several recipes and divide the text in to ingredients, cooking time, and them cooking steps, and use markovify to generate a new recipe on it's own?