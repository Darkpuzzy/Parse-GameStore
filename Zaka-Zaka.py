import requests
from bs4 import BeautifulSoup
from time import sleep
from fake_useragent import UserAgent

FUA = UserAgent().chrome
zaka_zaka = 'https://zaka-zaka.com/game/rising-storm-2-vietnam' # fallout-new-vegas

while True:
    sleep(3)
    req = requests.get(zaka_zaka, headers={'User-Agent': FUA})
    code_txt = req.text
    break

#call-of-cthulhu
#fallout-new-vegas
#subnautica
soup = BeautifulSoup(code_txt,'lxml')
old_price = soup.find_all('div', class_='old-price')
price_now = soup.find_all('div', class_='price')
discount = soup.find_all('div', class_='discount')

for key,value in req.request.headers.items():
    pass
    #print(key+':'+value)


def price_game(oldprice,price,discount):
    price_list = []
    find(obj=oldprice[-1],to_append=price_list)
    sleep(2)
    find(obj=price[-1],to_append=price_list)
    sleep(1)
    find(obj=discount[-1],to_append=price_list)
    price_dict = {'Old price':price_list[0],'Discount':f'{price_list[2]}'+"%",'Price':price_list[1]}
    return price_dict


def find(obj,to_append):
    for i in obj:
        to_str = str(i)
        a = to_str.strip('-%')
        if a.isdigit:
            go_int = int(a)
            to_append.append(go_int)
            return go_int

print(price_game(oldprice=old_price,price=price_now,discount=discount))
def main():
    pass

if __name__ == '__maim__':
    main()

