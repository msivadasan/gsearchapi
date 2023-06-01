# Google search API package

This package allows fetching of search result data using Google's JSON API. The code builds on Abdou Rockizk's code, provided here:
https://www.thepythoncode.com/article/use-google-custom-search-engine-api-in-python


## Inputs required

Instructions for creating programmable search engine and getting search engine id, and then obtaining the API key are available here:
https://developers.google.com/custom-search/v1/overview

## Key features

The package has two modules, mgsearch and searchprop.

First, initialize using search engine ID and API key:  
* x0=mgsearch.seid_apikey("YOUR_SEARCH_ENGINE_ID", "YOUR_API_KEY")

Now, we can search using a keyword:
* x1=x0.searchdata('YOUR_KEYWORD', PAGE_NUM, DATA_FILE_NAME)  
PAGE_NUM indicates which page of the search results is needed. The default is 1, which yields the first 10 search results. Changing to N will give the 10 results from the Nth page, i.e. results 10(N-1)+1 to 10N. 

DATA_FILE_NAME is the name of the .json file where all the search results are to be stored. This can include the path to the desired directory.

Here x1 is a dictionary object that contains all of the raw data (including metadata). The function result_dict in module "resultprop" allows users to extract variables from this raw data.
* x2=resultprop.result_dict(x1)

Now x2 has a number of useful attributes. Specifically:
* x2.items--> Dictionary of length 10 with each element having all of the data on that search result. E.g. x1.items[0] is a dictionary of all of the data on the first result.
* x2.long_desc--> Dictionary of length 10 with each element having the long description of the corresponding search result.
* x2.snippet--> Snippets of search results.
* x2.html_snippet--> HTML snippets of search results.
* x2.link--> URLs of search results.
* x2.title--> Titles of search results.

### Use of Cache

To avoid repeated calls with the same keyword and page number, we use python's inbuilt caching functionality lru_cache, so that the function searchdata runs only for unique calls. To see cache info:  
* print(x0.searchdata.cache_info()) 

To clear the cache:  
* x0.searchdata.cache_clear()

### Sample implementation
<pre><code>
import mgsearch  
import resultprop  
import json  

x0=mgsearch.seid_apikey("YOUR_SEARCH_ENGINE_ID", "YOUR_API_KEY")  

#Initializing the datafile to store results  
with open('rfile.json', 'w') as f:  
    json.dump({}, f, indent=4)  

for aa in ("Huawei",  "Lucent", "ATT", "Intel"):  
    x0.searchdata(aa, 1, 'rfile.json')  
     
#Load JSON file into dictionary  
with open('rfile.json') as f:  
    xx=json.load(f)  

#Use resultprop module to get attributes of a search result  
y1=resultprop.result_dict(xx['ATT_1'])  
print(y1.long_desc)  
"""  
Prints long description for the first page's 10 results for ATT:  
['Shop deals on unlimited data plans, Internet service, and DIRECTV STREAM. Get 24/7 support, pay your bills & manage your account online.', 'Find the latest AT&T news, including information on new devices, network services, mobile phones and technology.', "Shop AT&T's selection of smartphones, accessories & mobile phone plans. Learn about our best phone deals and wireless plans or get support & pay your bill.", 'Browse available job openings at AT&T', 'Get reliable, fast, and safe Internet from AT&T. View Internet plans, prices and offers available in your area!', 'Find right solution for your business from AT&T. Offering the latest business phones, data plans, IoT, Internet and Networking. Login to AT&T Business and manage your business services.', 'N/A', 'N/A', 'Get the latest in news, entertainment, sports, weather and more on Currently.com. Sign up for free email service with AT&T Yahoo Mail.', 'We create connection – with each other, with what people need to thrive in their everyday lives and with the stories and experiences that matter.']  
"""
</code></pre>
