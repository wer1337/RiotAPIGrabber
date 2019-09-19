"""
Riot uses a web service called Data Dragon to centralize all champion assets
As it stands, the champions.json file is absolutely  horrid to parse through
This tool will create my own personal json file for my program to use
"""
import requests
import json


def data():
    ddragon_url = "https://ddragon.leagueoflegends.com/cdn/9.18.1/data/en_US/champion.json"
    ddragon_json = requests.get(ddragon_url).json()['data']

    champions = {}

    for i in ddragon_json.values():
        champions.update({i['key']:i['id']})

    return champions


def main():
    champions = data()

    with open('champion.json', 'w', encoding='utf-8') as f:
        json.dump(champions, f, ensure_ascii=False, indent=4)

    return 0


if __name__ == '__main__':
    main()
