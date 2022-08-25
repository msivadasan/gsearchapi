# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 20:37:20 2022
@author: Madhav

I borrowed from Abdou Rockizk's code, provided here:
https://www.thepythoncode.com/article/use-google-custom-search-engine-api-in-python
To prevent API multiple times for the same keyword, using inbuilt lru_cache
"""
from functools import lru_cache
import requests

class seid_apikey():
    #print("This code requires both a search engine id and a api key")
    def __init__(self,apikey="missing",searchengid="missing"):
        if apikey=="missing" or searchengid=="missing":
            print('\033[41m'+"Input Error:"+'\033[0m', "This code requires both a search engine id and an api key. Instructions for setting up search engine id and getting an API key are available here: https://developers.google.com/custom-search/v1/overview") 
        else:
            # 
            self._API_KEY_ =apikey # User can provide own API Key
            # get your Search Engine ID on your CSE control panel
            self._SEARCH_ENGINE_ID_ = searchengid # User can provide own search engine id
            # the search query you want
      
    @lru_cache(maxsize=None)
    def searchdata(self, keyword, page=1): #default page num is 1, i.e., top 10 results
        # calculating start, (page=2) => (start=11), (page=3) => (start=21)
        start = (page - 1) * 10 + 1
        print("New search, so the API is called")
        return requests.get(f"https://www.googleapis.com/customsearch/v1?key={self._API_KEY_}&cx={self._SEARCH_ENGINE_ID_}&q={keyword}&start={start}").json()
            
 
