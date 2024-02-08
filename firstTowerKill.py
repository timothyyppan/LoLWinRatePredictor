import WinOrNot as won

def get_first_tower(match_info, summoner_name):
    first_tower = 0
    for participant in match_info['info']['participants']:
        if participant['firstTowerKill']:
            if won.get_win(match_info, participant['summonerName']) and won.get_win(match_info, summoner_name):
                first_tower = 1
    return first_tower