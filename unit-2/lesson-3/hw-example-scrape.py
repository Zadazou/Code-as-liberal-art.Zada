import requests
from bs4 import BeautifulSoup

crgslist_response = requests.get("https://www.allrecipes.com/recipe/244520/belizean-chicken-stew/")

crgslist_soup_html = BeautifulSoup(crgslist_response.text, "html.parser")

crgslist_text = crgslist_soup_html.get_text()

freeStuff = []

def getTitles(soupdata):
    titles = soupdata.select("p")
    if titles:
        for t in titles:
            freeStuff.append(t.get_text())

getTitles(crgslist_soup_html)

freeText = " ".join(freeStuff)

crgslist_data = open('recipe.txt', 'w')
crgslist_data.write(freeText)
crgslist_data.close()