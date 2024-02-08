import WinOrNot as won

def get_kill_death_ratio(match_info, summoner_name):
    winners = []
    winners_kills = 0.0
    winners_deaths = 0.0
    winners_kill_death_ratio = 0.0
    losers = []
    losers_kills = 0.0
    losers_deaths = 0.0
    losers_kill_death_ratio = 0.0
    for participant in match_info['info']['participants']:
        if won.get_win(match_info, participant['summonerName']) == 1:
            winners.append(participant['summonerName'])
            winners_kills += participant['kills']
            if participant['deaths'] == 0:
                winners_deaths += 1
            else:
                winners_deaths += participant['deaths']
        else:
            losers.append(participant['summonerName'])
            losers_kills += participant['kills']
            if participant['deaths'] == 0:
                losers_deaths += 1
            else:
                losers_deaths += participant['deaths']
    winners_kill_death_ratio = winners_kills/winners_deaths
    losers_kill_death_ratio = losers_kills/losers_deaths
    for winner in winners:
        if winner == summoner_name:
            return winners_kill_death_ratio/losers_kill_death_ratio
    return losers_kill_death_ratio/winners_kill_death_ratio