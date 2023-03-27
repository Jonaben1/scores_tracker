import requests
from bs4 import BeautifulSoup as bs
import pandas as pd




club_names = ['Arsenal', 'Aston Villa', 'Bournemouth', 'Brentford', 'Brighton', 'Chelsea', 'Crystal Palace', 'Everton', 'Fulham',
         'Leeds', 'Leicester', 'Liverpool', 'Manchester United', 'Manchester City', 'Newcastle', 'Nottingham Forest', 'Southampton',
         'Tottenham', 'West Ham', 'Wolves']


link = f'https://onefootball.com/en/competition/premier-league-9/fixtures'
# getting data
source = requests.get(link).text
# scraping the data
page = bs(source, 'lxml')



# searching for the date and time
dateTime = page.find_all('div', class_='simple-match-card__match-content')
date_time = []

for i in range(len(dateTime)):
    date_time.append(dateTime[i].text.strip())


#  searching for the teams

team = page.find_all('span',  class_='simple-match-card-team__name')
teams = []
for i in range(len(team)):
    teams.append(team[i].text.strip())

# separating the teams
home = []
for i in teams[0::2]:
    home.append(i)

away = []
for i in teams[1::2]:
    away.append(i)


# searching for the scores data
score = page.find_all('span', class_='simple-match-card-team__score')
scores = []
for i in range(len(score)):
    scores.append(score[i].text.split())

# separating the scores
home_scores = []
away_scores = []

for i in scores[0::2]:
    home_scores.append(i)

for i in scores[1::2]:
    away_scores.append(i)

# converting to Pandas DataFrame

df = pd.DataFrame({'Home': home, 'HG': home_scores, 'AG': away_scores, 'Away': away, 'Date_Time': date_time})

