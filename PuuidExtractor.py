import requests

def get_puuid(summoner_name, api_key):
    puuid_api_url = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summoner_name + '?api_key=' + api_key 
    
    puuid_response = requests.get(puuid_api_url)

    if puuid_response.status_code == 200:
        puuid_data = puuid_response.json()
        return puuid_data['puuid']
    else:
        print("Error: Puuid Extractor")
