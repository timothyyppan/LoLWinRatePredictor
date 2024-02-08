import requests
def get_match_id(puuid, api_key):
    match_id_api_url = 'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/' + puuid + '/ids?start=0&count=100&api_key=' + api_key
    
    match_id_response = requests.get(match_id_api_url)
    
    if match_id_response.status_code == 200:
        match_id = match_id_response.json()
        return match_id
    else:
        print("Error: Match ID Extractor")