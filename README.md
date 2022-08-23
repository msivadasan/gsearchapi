# Google search API package

This package alllows fetching of search result data using Google's JSON API. The code builds on Abdou Rockizk's code, provided here:
https://www.thepythoncode.com/article/use-google-custom-search-engine-api-in-python


## Inputs required

Instructions for creating programmable search engine and getting search engine id, and then obtaining the API key are available here:
https://developers.google.com/custom-search/v1/overview

### A sample search
The module mgsearch has two functions

First, initialize using search engine ID and API key:
x0=mgsearch.seid_apikey("YOUR_SEARCH_ENGINE_ID", "YOUR_API_KEY")

Now, we can search using a keyword
x1=x0.searchdata('YOUR_KEYWORD', PAGE_NUM)
PAGE_NUM indicates which page of the search results is needed. The default is 1, which yields the first 10 search results. Changing to N will give the 10 results from the Nth page, i.e. results 10(N-1)+1 to 10N. 

Here x1 is a dictionary object that contains all of the raw data (including metadata). The function result_dict in module "searchprop" allows users to extract variables from this raw data.
x2=resultprop.result_dict(x1)

Now x2 has a number of useful attributes. Specifically:
x2.items--> Dictionary of length 10 with each element having all of the data on that search result. E.g. x1.items[0] is a dictionary of all of the data on the first result.
x2.long_desc--> Dictionary of length 10 with each element having the long description of the corresponding search result.
x2.snippet--> Snippets of search results.
x2.html_snippet--> HTML snippets of search results.
x2.link--> URLs of search results.
x2.title--> Titles of search results.

### Use of Cache
To avoid repeated calls with the same keyword and page number, we use python's inbuilt caching functionality lru_cache. To see cache info:
print(x0.searchdata.cache_info())
To clear the cache:
x0.searchdata.cache_clear()


