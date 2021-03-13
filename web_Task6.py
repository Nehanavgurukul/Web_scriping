import json
from bs4 import BeautifulSoup
from pprint import pprint
import requests
from web_Task5 import *


def analyse_movies_language(movies_list):
        language_list = []
        for dic in movies_list:
                list1= dic["language"]
                for item in list1:
                        language_list.append(item)

        language_dict = {}
        for isLanguage in language_list:
                count = 0
                for lang in language_list:
                        if(isLanguage == lang):
                                count +=1
                language_dict[isLanguage] = count
        return language_dict


        return language_dict
analyse_language = analyse_movies_language(got_details_movie_list)
# pprint(analyse_language)

#  this line for see output only
with open("Task6.json" , "w") as Task6_file:
        json.dump(analyse_language,Task6_file)
