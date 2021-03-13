import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

first_reques = requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
py_data = first_reques.text

soup = BeautifulSoup(py_data,"html.parser")

list_position = []
list_name = []
list_year = []
list_rating = []
list_url = []

Main_List = []

def scrape_top_list():
    find_name = soup.find('div',class_= "lister")
    inside_find = find_name.find('tbody', class_= "lister-list")
    trs = inside_find.find_all('tr')
    
    
    position = 1
    for x in trs:
        list_position.append(position)
        name = x.find("td",class_= "titleColumn").a.get_text()
        list_name.append(name)

        year = x.find("td",class_= "titleColumn").span.get_text()
        list_year.append(int(year[1:5]))

        rating = x.find("td",class_= "ratingColumn imdbRating")
        list_rating.append(float(rating.get_text().strip()))

        link = x.find("td",class_= "titleColumn")
        link1 = link.find("a")
        list_url.append(link1.get("href"))
        position += 1


    i = 0
    for posi in list_name:
        dic = {}
        dic["name"] = list_name[i]
        dic["year"] = list_year[i]
        dic["position"] = list_position[i]
        dic["rating"] = list_rating[i]
        dic["url"] = "https://www.imdb.com"+list_url[i]
        Main_List.append(dic)
        i = i+1
    
    return Main_List

name = scrape_top_list()
# pprint(name)

# Blow line for seeing only data on json file bcz there can see full data properly:
with open ("Task1.json", "w") as Neha_file :
    json.dump(name , Neha_file)

