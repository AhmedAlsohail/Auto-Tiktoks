# import module
import requests
from bs4 import BeautifulSoup

# user define function
# Define the headers
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

# Scrape the data
def getdata(url):
	r = requests.get(url, headers = HEADERS)
	return r.text

def getContent(url):
    # pass the url
    # into getdata function
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')

    # display html code
    #print(soup)

    # find the Html tag
    # with find()
    # and convert into string
    data_str = ""
    result = ""
    for item in soup.find_all("div", class_="text-neutral-content md max-h-[253px] overflow-hidden s:max-h-[318px] m:max-h-[337px] l:max-h-[352px] xl:max-h-[452px] text-14"):
        data_str = data_str + item.get_text()
    return data_str