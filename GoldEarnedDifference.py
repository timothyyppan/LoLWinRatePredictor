import WinOrNot as won

def get_gold_difference(match_info, summoner_name):
    winners = []
    winners_gold = 0.0
    losers = []
    losers_gold = 0.0
    for participant in match_info['info']['participants']:
        if won.get_win(match_info, participant['summonerName']) == 1:
            winners.append(participant['summonerName'])
            winners_gold += participant['goldEarned']
        else:
            losers.append(participant['summonerName'])
            losers_gold += participant['goldEarned']
    for winner in winners:
        if winner == summoner_name:
            return winners_gold - losers_gold
    return losers_gold - winners_gold