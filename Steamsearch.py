import requests
from time import sleep
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from lxml import etree
from urllib.request import urlopen

enter = 'dayz'
FUA = UserAgent().chrome
steam = f'https://store.steampowered.com/search/?term=dayz' # Rising+Storm+2 #hitman+2
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

    if not list_links:
        interim_list = []
        j1 = tree.xpath(f"//div[@id='search_resultsRows']/a[1]")
        advac = j1[-1].attrib
        interim_list.append(advac['href'])
        game_name = spliter(list=interim_list,game_name=None)
        enter = game_name
        return links(arg=enter)
    return list_links


def counter(list_add: list):
    j = list_add
    count_cheak = j.count(enter)
    return count_cheak


def spliter(list,game_name):
    list_split = []
    n = 0
    game_n = game_name
    while n < len(list):
        for i in list:
            j = i.split('/')
            list_split.extend(j)
            n += 1

    if game_n != None:
        def find_game_id(list_cheaker,game):
            try:
                index_game = list_cheaker.index(game)
                print(index_game)
                game_id = list_cheaker[index_game - 1]
                return game_id
            except ValueError:
                ind = 0
                while True:
                    if game.lower() == list_cheaker[ind].lower():
                        game_id = list_cheaker[ind-1]
                        break
                    else:
                        ind += 1
                        continue
            return game_id
        return find_game_id(list_cheaker=list_split, game=game_n)
    else:
        return list_split[5]


def linkers(id,list_game):
    for j in list_game:
        if id in j:
            return j

""" PARSE PRICE """
html_link = linkers(id=spliter(links(enter),enter),list_game=links(enter))

while True:
    sleep(1)
    req = requests.get(html_link, headers={'User-Agent': FUA})
    code_txt = req.text
    break

soup = BeautifulSoup(code_txt,'lxml')
price = soup.find_all('script', type="text/javascript")
old_price = soup.find_all('div')   # 'div', 'data-price-final'  'meta', itemprop="price"
print(old_price)

print(f'________________________________________________________________________________________')
print(linkers(id=spliter(links(enter),enter),list_game=links(enter)))

#span[@class='title']
#for el in j:
    #print(el)
    #print(dir(el))
#GameName = i.findAll('a', class_ = 'search_result_row ds_collapse_flag')
# <meta itemprop="price" content="1199">
""" data-price-final="33100">
<div class="discount_pct">-80%</div>
<div class="discount_prices">
<div class="discount_original_price">1659 pуб. """

# <div class="game_purchase_price price" data-price-final="119900"



