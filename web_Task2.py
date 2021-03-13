import requests
from bs4 import BeautifulSoup
from web_Task1 import * 
from pprint import pprint
import json 

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
    
group_of_year = group_by_year(name)
# pprint(group_of_year)

# Blow line for seeing only data on json file bcz there can see full data properly:
with open ("Task2.json", "w") as data_File :
    json.dump(group_of_year, data_File)


