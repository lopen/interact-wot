import requests, json, re
from bs4 import BeautifulSoup as bs

places = {}
for place in json.load(open('markers.json'))['poi']:
    places[place['name']] = ""    # get all place names to scrape for

URL = "https://wot.fandom.com/wiki/"

for key in places.keys():
    page = requests.get(URL+key.replace(" ", "_"))

    soup = bs(page.content, "html.parser")

    results = soup.find_all("div", {"class": "mw-parser-output"})

    match = re.match(r'Description\-(.*?)\-Geography', str(soup))
    if match:
        print("hello", match.group())