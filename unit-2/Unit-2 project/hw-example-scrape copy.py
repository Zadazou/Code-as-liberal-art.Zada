import requests
from bs4 import BeautifulSoup

crgslist_response = requests.get("https://food52.com/recipes/20691-spicy-sesame-pork-soup-with-noodles")

crgslist_soup_html = BeautifulSoup(crgslist_response.text, "html.parser")

crgslist_text = crgslist_soup_html.get_text()

freeStuff = []

def getTitles(soupdata):
    titles = soupdata.select("li")
    #when select "p" it scrapes the stories section of the recipe. when select "li" it scrapes the ingredients and cooking instruction.
    if titles:
        for t in titles:
            freeStuff.append(t.get_text())

getTitles(crgslist_soup_html)

freeText = " ".join(freeStuff)

crgslist_data = open('steps4.txt', 'w')
crgslist_data.write(freeText)
crgslist_data.close()