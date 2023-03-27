import requests
import pandas as pd

# fetching goal assists data
assist = 'https://sports.ndtv.com/english-premier-league/stats/assists-player-statsdetail'
res = requests.get(assist)
d = pd.read_html(res.text, index_col=0)
assists = d[0]

# fetching goal scorers data
goal = 'https://sports.ndtv.com/english-premier-league/stats/top-goal-scorers-player-statsdetail'
get = requests.get(goal)
req = pd.read_html(get.text, index_col=0)
goals = req[0]

# fetching all time goal scorers
all_goals = 'https://www.premierleague.com/stats/top/players/goals'
g = requests.get(all_goals)
data = pd.read_html(g.text, index_col=0)
all_time_goals = data[0]
#dropping unnecessary columns
all_time_goals.drop(['Unnamed: 5'], axis=1, inplace=True)
# renaming a column
all_time_goals.rename(columns={'Stats': 'Goals'}, inplace=True)

# fetching all time assists
all_assists = 'https://www.premierleague.com/stats/top/players/goal_assist'
a = requests.get(all_assists)
df = pd.read_html(a.text, index_col=0)
all_time_assists = df[0]
#dropping unnecessary columns
all_time_assists.drop(['Unnamed: 5'], axis=1, inplace=True)
# renaming a column
all_time_assists.rename(columns={'Stats': 'Assists'}, inplace=True)
