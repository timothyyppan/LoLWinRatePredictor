import requests
import BaronKillsDifference as bkr
import championLevelDifference as clr
import dragonKillsDifference as dkr
import firstBloodKill as fbk
import firstTowerKill as ftk
import GoldEarnedDifference as ger
import inhibitorKillsDifference as ikr
import killsDeathsRatio as kdr
import totalMinionsKilledDifference as tmkr
import turretKillsDifference as tkr
import WinOrNot as won

def get_match_info(match_id, summoner_name, api_key):
    match_info_api_url = 'https://americas.api.riotgames.com/lol/match/v5/matches/' + match_id + '/timeline?api_key=' + api_key
    match_info_response = requests.get(match_info_api_url)
    
    if match_info_response.status_code == 200:
        match_info = match_info_response.json()

        interval = 70000
        current_interval = 0

        info = [] 
        win = []       
        temp = []
        for frame in match_info['info']['frames']:
            for event in frame['events']:
                if current_interval <= event['timestamp']:
                    temp = [bkr.get_baron_difference(match_info, summoner_name),
                            clr.get_level_difference(match_info, summoner_name),
                            dkr.get_dragon_difference(match_info, summoner_name),
                            fbk.get_first_blood(match_info, summoner_name),
                            ftk.get_first_tower(match_info, summoner_name),
                            ger.get_gold_difference(match_info, summoner_name), 
                            ikr.get_inhibitor_difference(match_info, summoner_name),
                            kdr.get_kill_death_ratio(match_info, summoner_name),
                            tmkr.get_minion_difference(match_info, summoner_name),
                            tkr.get_turret_difference(match_info, summoner_name)
                            ]
                    info.append(temp)
                    temp = []
                    temp = [won.get_win(match_info, summoner_name)]
                    win.append(temp)
                    current_interval += interval
        return info, win
    else:
        print("Error: Match Info Extractor")