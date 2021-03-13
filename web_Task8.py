import json
from bs4 import BeautifulSoup
from pprint import pprint
import requests


My_reques = requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
py_data = My_reques.text

soup = BeautifulSoup(py_data,"html.parser")

Top_Movies = []
def scrape_top_list():
    main_div = soup.find('div',class_='lister')
    tbody = main_div.find("tbody",class_="lister-list")
    trs = tbody.find_all('tr')

    Movie_ranks = []
    Movie_name = []
    Year_of_realease = []
    Movie_urls = []
    Movie_rating = [] 

    for tr in trs :
        position = tr.find('td',class_='titleColumn').get_text().strip()
        rank = ''
        for i in position:
            if '.' not in i:
                rank = rank+i
            else:
                break
        Movie_ranks.append(int(rank))

        title = tr.find('td',class_ ='titleColumn').a.get_text()
        Movie_name.append(title)

        Year = tr.find('td', class_='titleColumn').span.get_text()
        Year_of_realease.append(int(Year[1:5]))

        imdb_rating = tr.find('td',class_='ratingColumn imdbRating')
        Movie_rating.append(float(imdb_rating.get_text().strip()))
        # list_rating.append(float(rating.get_text().strip()))

        link = tr.find('td',class_='titleColumn').a['href']
        Movie_link = "https:www.imdb.com"+link
        Movie_urls.append(Movie_link)
        pprint(link)


    i = 0
    for posi in Movie_name:
        dic = {}
        dic["name"] = Movie_name[i]
        dic["year"] = Year_of_realease[i]
        dic["position"] = Movie_ranks[i]
        dic["rating"] = Movie_rating[i]
        dic["url"] = Movie_urls[i]
        Top_Movies.append(dic)
        i = i+1
    return (Top_Movies)

Movies_top = scrape_top_list()
# pprint(Movies_top)
# print(Movies_top)

def group_by_year(movies):
    years_list = []
    for small_dic in movies:
        for x in small_dic:
            if(x == "year"):
                years_list.append(small_dic[x])
    
    group_dic = {}
    for y in years_list:
        s_list = []
        for dic in movies:
            for x in dic:
                if(y == dic[x]):
                    s_list.append(dic)
        group_dic[y] = s_list
    return group_dic
    
group_of_year = group_by_year(Movies_top)
# pprint(group_of_year)

#  this line for see output only
with open("Task8.json" , "w") as Task8_file:
    json.dump(group_of_year,Task8_file)



