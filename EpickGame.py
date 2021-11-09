import requests
from time import sleep
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re

FUA = UserAgent().chrome
EpicParce = 'https://www.epicgames.com/store/ru/p/Fallout' #hitman-3 world-war-z


def cleaner(list_obj: list):
    for element in list_obj:
        if re.match("^[0-9]*\.?\,?[0-9]*", str(element)):
            return element
        else:
            continue


while True:
    sleep(3)
    req = requests.get(EpicParce, headers= {'User-Agent': FUA})
    epic_code = req.text
    break


soup = BeautifulSoup(epic_code,'lxml')
find_price = soup.find_all('span', class_="css-z3vg5b")
find_discount = soup.find_all('div',class_="css-1rcj98u")


def senders():
    price_list = []
    findprice(obj=find_price,list_add=price_list)
    findprice(obj=find_discount,list_add = price_list)
    m = discount_procent(to_add=price_list)
    if price_list == []:
        final = 'В данном магазине отсутствует товар,проверьте правильно ли вы написали.'
    elif len(price_list) > 1:
        final = {'Price': price_list[0],'Discount': m, 'Old Price': price_list[1]}
    else:
        final = {'Price': price_list[0]}
    return final


def findprice(obj, list_add: list):
    for d in obj:
        for dis in d:
            if '₽' in dis:
                to_str = str(dis)
                j2 = to_str.replace(u'\xa0', u' ')
                list_add.append(j2)
                return j2


def discount_procent(to_add: list):
    try:
        j0 = ''.join(filter(lambda x: x.isdigit(), to_add[0]))
        j1 = ''.join(filter(lambda x: x.isdigit(), to_add[1]))
        n0 = float_s(n=j0)
        n1 = float_s(n=j1)
        procent = (str(100 - ((n0 * 100) / n1)) + " %")
        return procent
    except IndexError:
        print('Скидки щас нет')
    return

def float_s(n):
    if len(n) >=5:
        to_str = str(n)
        new_n = to_str[:3]+'.'+to_str[3:]
        return float(new_n)
    else:
        return float(n)
print(senders())


# print(''.join(filter(lambda x: x.isdigit(), proc_list[0])))
#                if len(new_d) > 8:
#                    a = new_d.replace('\xa0', ' ')
#                    listprice.append(a)
#                    for x in listprice:
#                        if listprice.count(x) < 2:
#                            listprice.remove(x)
#                            if listprice.count(x) > 1:
#                                listprice.remove(x)
#                                j = listprice[0]
#                                j1 = j.replace('\xa0', ' ')
#                                list_add.append(j1)
#                                return j1
# print(''.join([x for x in '+7 (123) 4567890' if x.isdigit()]))