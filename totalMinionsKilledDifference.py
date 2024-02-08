import WinOrNot as won

def get_minion_difference(match_info, summoner_name):
    winners = []
    winners_minions = 0.0
    losers = []
    losers_minions = 0.0
    for participant in match_info['info']['participants']:
        if won.get_win(match_info, participant['summonerName']) == 1:
            winners.append(participant['summonerName'])
            winners_minions += participant['totalMinionsKilled']
        else:
            losers.append(participant['summonerName'])
            losers_minions += participant['totalMinionsKilled']
    for winner in winners:
        if winner == summoner_name:
            return winners_minions - losers_minions
    return losers_minions - winners_minions