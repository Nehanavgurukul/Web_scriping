import requests
from bs4 import BeautifulSoup
from pprint import pprint
#Here no need to import web_Task1 bcz web_Task2 is import so web_Task1 is already there:
from web_Task2 import *
import json


def group_by_decade(movies):
    # movies_by_year = group_by_year(movies)
    movies_by_decade = {}
    movies_1950 = []
    movies_1960 = []
    movies_1970 = []
    movies_1980 = []
    movies_1990 = []
    movies_2000 = []
    movies_2010 = []
    movies_2020 = []
    for dic in movies:
        for x in dic :
            if( x == "year"):
                if(1950 == dic[x] or 1960 > dic[x]):
                    movies_1950.append(dic)
                elif(1960 == dic[x] or 1970 > dic[x]):
                    movies_1960.append(dic)
                elif(1970 == dic[x] or 1980 > dic[x]):
                    movies_1970.append(dic)
                elif(1980 == dic[x] or 1990 > dic[x]):
                    movies_1980.append(dic)
                elif(1990 == dic[x] or 2000 > dic[x]):
                    movies_1990.append(dic)
                elif(2000 == dic[x] or 2010 > dic[x]):
                    movies_2000.append(dic)
                elif(2010 == dic[x] or 2020 > dic[x]):
                    movies_2010.append(dic)

    movies_by_decade["1950"] = movies_1950
    movies_by_decade["1960"] = movies_1960
    movies_by_decade["1970"] = movies_1970
    movies_by_decade["1980"] = movies_1980
    movies_by_decade["1990"] = movies_1990
    movies_by_decade["2000"] = movies_2000
    movies_by_decade["2010"] = movies_2010
    movies_by_decade["2020"] = movies_2020
    return movies_by_decade

data3 = group_by_decade(name)
# pprint(data3)


# Blow line for seing data on json file bcz there can see full data properly:
with open ("Task3.json", "w") as Neha_file :
    json.dump(data3 , Neha_file)

    
