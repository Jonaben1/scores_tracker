import pandas as pd
import requests
import lxml
from bs4 import BeautifulSoup as bs

link = f'https://onefootball.com/en/competition/premier-league-9/table'
# getting the data
source = requests.get(link).text
# scraping the data
page  = bs(source, 'lxml')
# filtering the data based on a defined CSS class
fix = page.find_all('a', class_='standings__row-grid')

tab = []
for i in range(len(fix)):
    tab.append(fix[i].text.split())

# rearranging the table
def arrange_table():
    dd = []
    pos = []
    for i in tab:
        if len(i) == 8:
            dd.append(i[1:])
        elif len(i) == 9:
            dd.append([f'{i[1]} {i[2]}', i[3], i[4], i[5], i[6], i[7], i[8]])
        pos.append(i[0])
    return dd, pos


dd, pos = arrange_table()
columns = ['Club', 'MP', 'W', 'D', 'L', 'GD', 'PTS']
table = pd.DataFrame(dd, columns=columns, index=pos)


















