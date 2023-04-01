import requests,json
import pandas as pd
from api_keys import Get_Your_Own_Key

url = "https://free-nba.p.rapidapi.com/teams"

querystring = {"page":"0","per_page":"25"}

headers = {
	"X-RapidAPI-Key" : f'{Get_Your_Own_Key}',
	"X-RapidAPI-Host": "free-nba.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
response_info = response.json()
pretty_json= json.dumps(response_info,indent=2)
final= json.loads(pretty_json)

teams = {'Atlanta hawks':0,
	 'Boston celtics':1,
	 'Brooklyn nets':2,
	 'Charlotte hornets':3,
	 'Chicago bulls':4,
	 'Cleveland cavaliers':5,
	 'Dallas Mavericks':6,
	 'Denver Nuggets':7,
	 'Detroit Pistons':8,
	 'Golden state warriors':9,
	 'Houston Rockets':10,
	 'Indiana Pacers':11,
	 'Los Angeles Clippers':12,
	 'Los Angeles Lakers':13,
	 'Memphis Grizzlies':14,
	 'Miami Heat':15,
	 'Milwaukee bucks':16,
	 'Minnesota timberwolves':17,
	 'New orleans pelicans':18,
	 'New York knicks':19,
	 'Oklahoma City thunder':20,
	 'Orlando Magic':21,
	 'Philadelphia 76ers':22,
	 'Phoenix suns':23,
	 'Portland Trailblazers':24
	 }

for x in teams:
	print(x)

Choose = input("which team do you choose?")

if Choose in teams:
	print (final['data'][teams[Choose]])