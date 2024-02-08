def get_win(match_info, summoner_name):
    for participant in match_info['info']['participants']:
        if (participant['summonerName'] == summoner_name) and participant['win']:
            return 1
    return 0