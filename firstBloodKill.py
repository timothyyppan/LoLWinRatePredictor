import WinOrNot as won

def get_first_blood(match_info, summoner_name):
    first_blood = 0
    for participant in match_info['info']['participants']:
        if participant['firstBloodKill']:
            if won.get_win(match_info, participant['summonerName']) and won.get_win(match_info, summoner_name):
                first_blood = 1
    return first_blood