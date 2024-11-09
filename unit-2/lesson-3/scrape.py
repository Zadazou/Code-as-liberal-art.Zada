# import the requests library
import requests

# import beautifulsoup
from bs4 import BeautifulSoup

blog_response = requests.get("https://food52.com/recipes/372-salmorejo-cordobes")
#requesting data from the website. I used a recipe website and the recipe is for braised beef. I wonder if I can get the markovify to generate a recipe and see how well it works


blog_soup_html = BeautifulSoup(blog_response.text, "html.parser")
# using beautifulsoup to get the data

blog_soup_text = blog_soup_html.get_text()
# using beautiful soup to get the text from the website
blog_data = open('soup.txt', 'w')
# opening a new text file named "braised beef" in writing mode
blog_data.write(blog_soup_text)
# writing the text from the website into the text file 
blog_data.close()
# close the file
with open( 
    "soup.txt", 'r') as r, open( 
        'soup-output.txt', 'w') as o: 
    # openning the braise beef text file to read, and open a new text file called output to write
      
    for line in r: 
       
        if not line.isspace(): 
            o.write(line) 
  # .isspace checks for lines that are empty, if the line is not empty it gets write into output.txt
o.close()
# close output file


def getTitles(soupdata):  
  titles = soupdata.select("h2")
  if titles:
    for t in titles:
      print(t.text)
      #getting the titles form the text we craped from the website. I wonder what we can put instead of h2 to get diferent out come. I tried inspecting the website but I don't know where to find the counterparts of h2.
print("blog........")
getTitles(blog_soup_html)
