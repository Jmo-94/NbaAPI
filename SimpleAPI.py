import requests,json
import pandas as pd
from api_keys import Get_Your_Own_Key

#Obtaining info from free NBA rapid API, you can obtain key by signing up
url = "https://free-nba.p.rapidapi.com/players"

querystring = {"page":"0","per_page":"25"}

headers = {
	"X-RapidAPI-Key" : f'{Get_Your_Own_Key}',
	"X-RapidAPI-Host": "free-nba.p.rapidapi.com"
}

#formatting API response
response = requests.request("GET", url, headers=headers, params=querystring)
response_info = response.json()
pretty_json= json.dumps(response_info,indent=2)
final= json.loads(pretty_json,)


#empty list to organize later in a table
nbateam=[]
firstName=[]
lastname=[]

#Using list to parse through first names and adding a first name to the empty list firstname
Name = range(len(final['data']))
for value in Name:
	firstName.append(final['data'][value]['first_name'])

#Using list to parse through last names and adding a last name to the empty list lastname
last = range((len(final['data'])))
for value in last:
 	lastname.append((final)['data'][value]['last_name'])

#Using list to parse through teams and adding a team to the empty list nbateam
team = range((len(final['data'])))
for value in team:
	nbateam.append((final['data'][value]['team']['full_name']))

#Used zip to combine a set of lists together
Zipped = pd.DataFrame(list(zip(firstName,lastname,nbateam)),
columns = ['First','Last','Team'])
#output [(Ron,Baker,New York Knicks)(Jabari,Bird, Boston Celtics)]

#used pandas to format tables
pd.set_option('display.max_rows', None)

print(Zipped.to_string(index=False))




