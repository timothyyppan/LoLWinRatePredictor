import WinOrNot as won

def get_dragon_difference(match_info, summoner_name):
    winners = []
    winners_dragons = 0.0
    losers = []
    losers_dragons = 0.0
    for participant in match_info['info']['participants']:
        if won.get_win(match_info, participant['summonerName']) == 1:
            winners.append(participant['summonerName'])
            winners_dragons += participant['dragonKills']
        else:
            losers.append(participant['summonerName'])
            losers_dragons += participant['dragonKills']
    for winner in winners:
        if winner == summoner_name:
            return winners_dragons - losers_dragons
    return losers_dragons - winners_dragons