import KillerPlayerTeamId as kpti

def get_baron_difference(match_info, summoner_name):
    player_team_barons = 0.0
    enemy_team_barons = 0.0
    player_team_id = kpti.get_killer_player_team_id(match_info, summoner_name)
    for frame in match_info['info']['frames']:
            for event in frame['events']:
                if event['type'] == "ELITE_MONSTER_KILL" and event['monsterType'] == "BARON_NASHOR":
                    if event['killerTeamId'] == player_team_id:
                        player_team_barons += 1
                    else:
                        enemy_team_barons += 1
    print(player_team_barons - enemy_team_barons)
    return player_team_barons - enemy_team_barons