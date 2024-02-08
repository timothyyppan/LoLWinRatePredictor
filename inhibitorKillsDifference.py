import WinOrNot as won

def get_inhibitor_difference(match_info, summoner_name):
    winners = []
    winners_inhibitors = 0.0
    losers = []
    losers_inhibitors = 0.0
    for participant in match_info['info']['participants']:
        if won.get_win(match_info, participant['summonerName']) == 1:
            winners.append(participant['summonerName'])
            winners_inhibitors += participant['inhibitorKills']
        else:
            losers.append(participant['summonerName'])
            losers_inhibitors += participant['inhibitorKills']
    for winner in winners:
        if winner == summoner_name:
            return winners_inhibitors - losers_inhibitors
    return losers_inhibitors - winners_inhibitors