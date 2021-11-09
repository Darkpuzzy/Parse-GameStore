import requests
from time import sleep
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from lxml import etree
from urllib.request import urlopen

enter = 'DayZ'
FUA = UserAgent().chrome
steam = f'https://store.steampowered.com/search/?term=DayZ' # Rising+Storm+2 #hitman+2
HTMLPARCE = etree.HTMLParser()


while True:
    sleep(5)
    req_link = requests.get(steam, headers={'User-Agent':FUA})
    sleep(5)
    codetxt = req_link.text
    break


soup = BeautifulSoup(codetxt,'lxml')
result = soup.find_all('div', id = 'search_resultsRows')
#list_result = soup.find_all(lambda tag: tag.name == 'a' and tag.get('href') )
#print(result)
with open('SteamHTML', 'w', encoding='utf-8') as f:
    f.write(codetxt)

local = 'file:///C:/Python/Doc/Новая папка/PyCharm Community Edition 2021.1.2/game/SteamHTML' #C:\Python\Doc\Новая папка\PyCharm Community Edition 2021.1.2\game
respones = urlopen(local)
tree = etree.parse(respones,HTMLPARCE)


def links(arg: str):
    list_links = []
    for n in range(1,20):
        j = tree.xpath(f"//div[@id='search_resultsRows']/a[{n}]")
        advacii = j[-1].attrib
        if arg in advacii['href']:
            list_links.append(advacii['href'])
        elif arg.capitalize() in advacii['href']:
            list_links.append(advacii['href'])
        elif arg.upper() in advacii['href']:
            list_links.append(advacii['href'])
    return list_links


def counter(list_add: list):
    j = list_add
    count_cheak = j.count(enter)
    return count_cheak
    #if count_cheak == 19:

#span[@class='title']

#print(advacii)
print(links(enter))
print(f'________________________________________________________________________________________')
print(counter(links(enter)))
#span[@class='title']
#for el in j:
    #print(el)
    #print(dir(el))
#GameName = i.findAll('a', class_ = 'search_result_row ds_collapse_flag')



