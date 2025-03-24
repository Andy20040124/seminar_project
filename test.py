import requests
import shutil
from bs4 import BeautifulSoup # get clean data
from googlesearch import search #google search for the content
import sumy

url = 'https://pipingtech.com/resources/faqs/what-is-u-stamp-certification/'
keyword = "U-stamp"
web = requests.get(url)
web.encoding = "utf-8"
soup = BeautifulSoup(web.text, "html.parser")
dived = soup.find_all('div')
paragraph = [ct.get_text(strip=True) for ct in dived if keyword in ct.get_text()]
print(paragraph)