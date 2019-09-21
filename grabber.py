import yaml
import summoner_info as si
import match_info as mi
# Obtains champions name, returns as a dict

def main():
    # region = input("Input Region: ")
    # Going to default region to na1 since it's for personal usage
    region = 'na1'
    # summ_name = input("Input Summoner Name: ")
    summ_name = 'Alteration'

    # Summoner Information
    response_json = si.req_summ_data(region, summ_name, api_key)
    print(f"{summ_name} is level: {response_json['summonerLevel']}\n"
          f"Here are the last 10 Games Played\n")

    # Getting Match History
    mi.match_history(region, response_json['accountId'], api_key)

    # Getting match information of a specific game


if __name__ == "__main__":
    with open("app_config.yml", "r") as config_file:
        APP_CONFIG = yaml.safe_load(config_file)
    try:
        api_key = APP_CONFIG.get("api_key")
        main()
    except Exception as ex:
        print(f"Exception: {repr(ex)}")
