# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 17:34:08 2022
@author: Madhav
Borrows from Abdou Rockizk's code, provided here:
https://www.thepythoncode.com/article/use-google-custom-search-engine-api-in-python
"""
# This module helps extract specific subcomponents of the google search result headers
class result_dict():
    def __init__(self, input):
        self.input=input 
    
    # all of information in the 10 search item headers
    @property
    def items(self): #default page num is 1, i.e., top 10 results
        return self.input.get("items")
 
    # long description        
    @property
    def long_desc(self): #default page num is 1, i.e., top 10 results
        locallist=[]
        for i, search_item in enumerate(self.items, start=1):
            try:
                locallist.append(search_item["pagemap"]["metatags"][0]["og:description"])
            except KeyError:
                locallist.append("N/A")
        return locallist
        
    # page snippet
    @property
    def snippet(self):
        locallist=[]
        for i, search_item in enumerate(self.items, start=1):
            locallist.append(search_item.get("snippet"))
        return locallist
        
    # alternatively, you can get the HTML snippet (bolded keywords)
    @property
    def html_snippet(self):
        locallist=[]
        for i, search_item in enumerate(self.items, start=1):
            locallist.append(search_item.get("htmlSnippet"))
        return locallist
    
    # extract the page url        
    @property
    def link(self):
        locallist=[]
        for i, search_item in enumerate(self.items, start=1):
            locallist.append(search_item.get("link"))
        return locallist
    
    # get the page title
    @property
    def title(self):
        locallist=[]
        for i, search_item in enumerate(self.items, start=1):
            locallist.append(search_item.get("title"))
        return locallist
    
    
    
 
    
    
    