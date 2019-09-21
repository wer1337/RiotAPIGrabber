import requests


# Obtains summoner info through Riot API, returns json
def req_summ_data(region, summ_name, api_key):
    url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summ_name}?api_key={api_key}"
    return requests.get(url).json()
