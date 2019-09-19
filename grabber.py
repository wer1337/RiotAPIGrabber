import requests
import datetime
import yaml
import json


def get_champ_name():
    # Loads the json file
    with open("tools/champion.json") as f:
        loaded_json = json.load(f)

    return loaded_json


def req_summ_data(region, summ_name):
    url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summ_name}?api_key={api_key}"
    return requests.get(url).json()


def match_history(region, account_id):
    url = f"https://{region}.api.riotgames.com/lol/match/v4/matchlists/by-account/{account_id}?api_key={api_key}"

    matches = requests.get(url).json()['matches']
    champ_json = get_champ_name()

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


def main():
    # region = input("Input Region: ")
    # Going to default region to na1 since it's for personal usage
    region = 'na1'
    # summ_name = input("Input Summoner Name: ")
    summ_name = 'Alteration'

    # Summoner Information
    response_json = req_summ_data(region, summ_name)
    print(f"{summ_name} is level: {response_json['summonerLevel']}\n"
          f"Here are the last 10 Games Played\n")

    # Getting Match History
    match_history(region, response_json['accountId'])


if __name__ == "__main__":
    with open("app_config.yml", "r") as config_file:
        APP_CONFIG = yaml.safe_load(config_file)
    try:
        api_key = APP_CONFIG.get("api_key")
        main()
    except Exception as ex:
        print(f"Exception: {repr(ex)}")
