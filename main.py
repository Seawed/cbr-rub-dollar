import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

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
        date = str(today.year)+'.' + str(today.month)+'.' + str(today.day)

df = pd.DataFrame({'Date': [date],
                   'Salary': [str(dollar2)[:-1]]})
df.to_csv('my_csv.csv', mode='a', header=False)
