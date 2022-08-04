# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 20:37:20 2022
@author: Madhav
"""
"""
I borrowed from Abdou Rockizk's code, provided here:
https://www.thepythoncode.com/article/use-google-custom-search-engine-api-in-python
Need to execute the following first
pip3 install requests

I didn't want to call API multiple times for the same keyword. 
Based on intenet seraches, tried inbuilt lru_cache, which failed 1st time as class did not recognize duplicates
Found code to adress this problem on stack exchange:
https://stackoverflow.com/questions/53046304/how-to-cache-a-property-at-class-level-in-python
"""

class NameSingleton(type):
    def __init__(cls, *args, **kwargs):
        cls._instances = {}

    def __call__(cls, keyword, *args, **kwargs):
        try:
            return cls._instances[keyword]
        except KeyError:
            instance = super().__call__(keyword, *args, **kwargs)
            cls._instances[keyword] = instance
            return instance
        
class gsearch(metaclass=NameSingleton):
    from functools import lru_cache
        
    def __init__(self,keyword):
        self.keyword=keyword
        #import requests
        # get the API KEY here: https://developers.google.com/custom-search/v1/overview
        API_KEY = "AIzaSyC2y62k8yyeXS69noP0y9XNUl8s_PHb-MA"
        # get your Search Engine ID on your CSE control panel
        SEARCH_ENGINE_ID = "54b9ad3da1c1e450f"
        # the search query you want
        query = keyword
        # using the first page
        page = 1
        # constructing the URL
        # doc: https://developers.google.com/custom-search/v1/using_rest
        # calculating start, (page=2) => (start=11), (page=3) => (start=21)
        start = (page - 1) * 10 + 1
        self.url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"
        
        
    @property
    @lru_cache(maxsize=None)
    def fulldata(self):
        import requests
        print("The API is called")
        return requests.get(self.url).json()
        
    #defining some more attributes as lists
    @property
    def searchitems(self):
        return self.fulldata.get("items")    
    
    @property
    def long_desc(self):
        locallist=[]
        for i, search_item in enumerate(self.searchitems, start=1):
            try:
                locallist.append(search_item["pagemap"]["metatags"][0]["og:description"])
            except KeyError:
                locallist.append("N/A")
        return locallist
    
    # page snippet
    @property
    def snippet(self):
        locallist=[]
        for i, search_item in enumerate(self.searchitems, start=1):
            locallist.append(search_item.get("snippet"))
        return locallist
        
    # alternatively, you can get the HTML snippet (bolded keywords)
    @property
    def html_snippet(self):
        locallist=[]
        for i, search_item in enumerate(self.searchitems, start=1):
            locallist.append(search_item.get("htmlSnippet"))
        return locallist
    
    # extract the page url        
    @property
    def link(self):
        locallist=[]
        for i, search_item in enumerate(self.searchitems, start=1):
            locallist.append(search_item.get("link"))
        return locallist
    
    # get the page title
    @property
    def title(self):
        locallist=[]
        for i, search_item in enumerate(self.searchitems, start=1):
            locallist.append(search_item.get("title"))
        return locallist

"""
x1=(gsearch('Python'))
print(x1.link[3])
for aa in range (0, len(x1.searchitems)):
    print("Long Description for result",aa+1,":", x1.long_desc[aa])
"""



