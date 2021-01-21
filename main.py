import requests
from bs4 import BeautifulSoup
from datetime import datetime

if __name__ == '__main__':
    test = requests.get('https://www.cbr.ru/')
    with open('test.txt', 'wb') as f:
        f.write(test.content)

    with open("test.txt", "r", encoding="utf8") as f:
        contents = f.read()

        soup = BeautifulSoup(contents, 'lxml')

        curr = soup.findAll("div", {"class": "col-md-2 col-xs-9 _right mono-num"})
        dollar2 = curr[1].text.split()
        dollar2 = ''.join(dollar2)
        today = datetime.today()
        print('$ =', dollar2, 'time =', today.year,'-', today.month,'-', today.day)
        #   print("Current day:", today.hour)
