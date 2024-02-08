import WinOrNot as won

def get_level_difference(match_info, summoner_name):
    winners = []
    winners_levels = 0.0
    losers = []
    losers_levels = 0.0
    for participant in match_info['info']['participants']:
        if won.get_win(match_info, participant['summonerName']) == 1:
            winners.append(participant['summonerName'])
            winners_levels += participant['champLevel']
        else:
            losers.append(participant['summonerName'])
            losers_levels += participant['champLevel']
    for winner in winners:
        if winner == summoner_name:
            return winners_levels - losers_levels
    return losers_levels - winners_levels