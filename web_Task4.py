import json
from bs4 import BeautifulSoup
from pprint import pprint
import requests
from web_Task1 import *


def scrape_movie_details (movie_url):
        request = requests.get(movie_url)
        get_data = request.text
        soup1 = BeautifulSoup(get_data,"html.parser")
        Find_data = soup1.find('div',class_="title_wrapper").h1.get_text()


        movie_name = " "
        for i in Find_data:
                if("(" not in i):
                        movie_name = (movie_name+i).strip()
                else:
                        break

        sub_div = soup1.find('div',class_ ="subtext")
        RunTime = sub_div.find("time").get_text().strip()
        Hours_Time = int(RunTime[0])*60
        # print(Hours_Time)
        if 'min' in RunTime:
                runtime_minites = int(RunTime[3:].strip('min'))
                movie_runtime = Hours_Time + runtime_minites
                # print(movie_runtime)
        else:
             movie_runtime = Hours_Time


        gener = sub_div.find_all('a')
        gener.pop()
        # gener.pop()
        movie_gener = [i.get_text() for i in gener]
        # print(movie_gener)
        summary = soup1.find('div', class_ = "plot_summary")
        movie_bio = summary.find('div', class_ = "summary_text").get_text().strip()
        # print(movie_bio)

        Director = summary.find('div', class_ = "credit_summary_item")
        Director_List = Director.find_all('a')
        Movie_Directors = [i.get_text().strip() for i in Director_List]

        
        extra_details = soup1.find('div', attrs={"class":"article","id":"titleDetails"})
        list_of_divs = extra_details.find_all('div')
        for x in list_of_divs:
                tag4 = x.find_all('h4')
                for y in tag4:
                        if "Language:" in y:
                                Tag_anchor = x.find_all('a')
                                Movie_Language =[]
                                for language in Tag_anchor:
                                        Movie_Language.append(language.get_text())
                        elif "Country:" in y:
                                Tag_anchor = x.find_all('a')
                                Movie_Country = []
                                for country in Tag_anchor:
                                        Movie_Country.append(country.get_text())
        Movie_poster_link = soup1.find('div',class_ = "poster").a['href']
        Movie_poster = "https://www.imdb.com/" + Movie_poster_link

        # movie details dict..........
        Movie_Details_Dict = {}
        Movie_Details_Dict["name"] = movie_name
        Movie_Details_Dict["director"] = Movie_Directors
        Movie_Details_Dict["country"] = Movie_Country
        Movie_Details_Dict["language"] = Movie_Language
        Movie_Details_Dict["poster_image_url"] = Movie_poster
        Movie_Details_Dict["bio"] = movie_bio
        Movie_Details_Dict["runtime"] = movie_runtime
        Movie_Details_Dict["gener"] = movie_gener
        return Movie_Details_Dict
user_URL = int(input("Enter the URL choise"))
correct_URl = name[user_URL-1]["url"]
Movie_Details = scrape_movie_details (correct_URl)
# pprint(Movie_Details)

# Blow line for seing data on json file bcz there can see full data properly:
with open ("Task4.json", "w") as Task4_file :
    json.dump(Movie_Details ,Task4_file)

    
