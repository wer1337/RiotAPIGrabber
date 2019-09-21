import requests
import datetime
import champ_name as cname

def match_history(region, account_id, api_key):
    url = f"https://{region}.api.riotgames.com/lol/match/v4/matchlists/by-account/{account_id}?api_key={api_key}"

    matches = requests.get(url).json()['matches']
    champ_json = cname.get_champ_name()

    for i in range(10):
        match_id = matches[i]['gameId']
        lane = matches[i]['lane']

        # Sometimes the API doesn't have lane inforamtion
        # Will change this to check for ARAM
        if lane == 'NONE':
            lane = 'UNKNOWN'

        # Converts ms timestamp to normal people timestamp in format of Mon Day Year
        timestamp = datetime.datetime.fromtimestamp(matches[i]['timestamp'] / 1000).strftime("%b %d %Y")
        print(f"Match ID: {match_id:^20} Champion: {champ_json[str(matches[i]['champion'])]:^20} Lane: {lane:^20} Time: {timestamp}")
