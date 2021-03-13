import json
from bs4 import BeautifulSoup
from pprint import pprint
import requests
from web_Task5 import *

def  analyse_movies_directors (movie_list):
        director_list = []
        for dic in movie_list:
               list1 = dic["director"]
               for director in list1:
                       director_list.append(director)
        director_dic = {}
        for isDirector in director_list:
                count = 0
                for direct in director_list:
                        if(isDirector == direct):
                                count +=1
                director_dic[isDirector] = count
        return director_dic


        
analyse_directors = analyse_movies_directors(got_details_movie_list)
# pprint(analyse_directors)

#  this line for see output only
with open("Task7.json" , "w") as Task7_file:
        json.dump(analyse_directors,Task7_file)
