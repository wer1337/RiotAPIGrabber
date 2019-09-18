import requests
import datetime

APIKey = <INSERT YOUR OWN>

def get_champ_name(champ_id):
    champions = requests.get('https://ddragon.leagueoflegends.com/cdn/9.18.1/data/en_US/champion.json').json()['data']

    # Loops through champions list from ddragon
    for i in champions.values():
        # Compares the champion key '1-xxx' to the given id
        if int(i['key']) == champ_id:
            # Returns name of champion
            return i['id']
    # If invalid number returns 'None" str
    return 'None'


def req_summ_data(region, summ_name):
    url = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summ_name + "?api_key=" + APIKey

    return requests.get(url).json()


def match_history(region, summ_name, account_id):
    url = "https://" + region + ".api.riotgames.com/lol/match/v4/matchlists/by-account/" + account_id +"?api_key=" + APIKey

    matches = requests.get(url).json()['matches']

    for i in range(10):
        match_id = matches[i]['gameId']
        champ_name = get_champ_name(matches[i]['champion'])
        lane = matches[i]['lane']

        # Sometimes the API doesn't have lane inforamtion
        # Will change this to check for ARAM
        if lane == 'NONE':
            lane = 'UNKNOWN'

        # Converts ms timestamp to normal people timestamp in format of Mon Day Year
        timestamp = datetime.datetime.fromtimestamp(matches[i]['timestamp'] / 1000).strftime("%b %d %Y")
        print(f"Match ID: {match_id:^20} Champion: {champ_name:^20} Lane: {lane:^20} Time: {timestamp}")
    return 0


def main():
    region = input("Input Region: ")
    summ_name = input("Input Summoner Name: ")

    # Summoner Information
    response_json = req_summ_data(region, summ_name)
    print(f"{summ_name} is level: {response_json['summonerLevel']}\n"
          f"Here are the last 10 Games Played\n")

    # Getting Match History
    match_history(region, summ_name, response_json['accountId'])


if __name__ == "__main__":
    main()
