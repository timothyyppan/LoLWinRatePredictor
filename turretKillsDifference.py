import WinOrNot as won

def get_turret_difference(match_info, summoner_name):
    winners = []
    winners_turrets = 0.0
    losers = []
    losers_turrets = 0.0
    for participant in match_info['info']['participants']:
        if won.get_win(match_info, participant['summonerName']) == 1:
            winners.append(participant['summonerName'])
            winners_turrets += participant['turretKills']
        else:
            losers.append(participant['summonerName'])
            losers_turrets += participant['turretKills']
    for winner in winners:
        if winner == summoner_name:
            return winners_turrets - losers_turrets
    return losers_turrets - winners_turrets