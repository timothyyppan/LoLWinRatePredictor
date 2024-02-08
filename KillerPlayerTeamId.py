import ApiKeyGetter as akg
import PuuidExtractor as pe

def get_killer_player_team_id(match_info, summoner_name):
    api_key = akg.get_api_key()
    puuid = pe.get_puuid(summoner_name, api_key)
    for participant in match_info['info']['participants']:
        if participant['puuid'] == puuid:
            if participant['participantId'] <= 5:
                return 100
            else:
                return 200
