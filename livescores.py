import requests
import json

url = "https://api.sofascore.com/api/v1/sport/football/events/live"

payload = ""
headers = {
    'authority': "api.sofascore.com",
    'accept': "*/*",
    'accept-language': "en-US,en;q=0.9",
    'cache-control': "max-age=0",
    'if-none-match': "W/^\^a0b0d8cef2^^",
    'origin': "https://www.sofascore.com",
    'referer': "https://www.sofascore.com/",
    'sec-ch-ua': "^\^"
    }

response = requests.request("GET", url, data=payload, headers=headers)

jsondata = json.loads(response.text)

for game in jsondata['events']:
    league = game['tournament']['name']
    hometeam = game['homeTeam']['name']
    awayteam = game['awayTeam']['name']
    homescore = game['homeScore']['current']
    awayscore = game['awayScore']['current']
    print(league, " | ", hometeam, homescore, " - ", awayscore, awayteam,)